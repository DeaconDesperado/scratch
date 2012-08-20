import os
from pxquilt.listener import application
from pxquilt.config import TestingConfig
import unittest
import json
from pxquilt.encoder import Encoder, Decoder
from pxquilt.models.user import User
import logging
import logging.handlers
import re

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
log_format = logging.Formatter('\n%(asctime)s - %(message)s')
sh.setFormatter(log_format)
log.addHandler(sh)

class PXQuiltTest(unittest.TestCase):

    def setUp(self):
        application.config.from_object(TestingConfig)
        application.testing = True
        self.app = application.test_client()

    def login(self,username,password):
        resp = self.app.post('/data/login',data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
        return resp

    def logout(self):
        return self.app.get('/logout',follow_redirects=True)

    def tearDown(self):
        pass

    def decode_status(self,resp):
        return json.loads(resp.data)['flag']

    def test_a_register(self):
        log.info('Testing registration')
        def run():
            resp = self.app.post('/data/register',data={
                'username':'testuser',
                'password':'foobar'
            })
            return resp
        
        log.info('Testing first user')
        self.assertEqual(self.decode_status(run()),1)
        log.info('Testing dupe user, should reject')
        self.assertEqual(self.decode_status(run()),0)

    def test_b_login(self):
        log.info('Testing good login credentials')
        self.assertEqual(self.decode_status(self.login('testuser','foobar')),1)
        log.info('Testing bad login credentials')
        self.assertEqual(self.decode_status(self.login('brack','foo')),0)

    def test_c_twitter(self):
        log.info('Testing app auth urls for twitter')
        resp = self.app.get('/oauth/twitter')
        self.assertEquals(resp.status,'302 FOUND')
        self.assertTrue(re.match('^https://api\.twitter\.com.',resp.location))

    def test_d_submit_patch(self):
        def run():
            resp = self.app.post('/data/patch/126/126',data={'image_file':open('ahri.png')})
            return resp
        log.info('Testing patch submission for unauthenticated user')
        self.assertEqual(self.decode_status(run()),0)
        self.login('testuser','foobar')
        log.info('Testing patch submission for authenticated user')
        good_patch = run()
        self.patch_id = json.loads(good_patch.data)['patch']['_id']
        log.info('Patch ID: %s',self.patch_id)
        self.assertEqual(self.decode_status(good_patch),1)

    def test_e_vote_patch(self):
        resp = self.app

def tearDownModule():
    log.info('dropping database')
    User.connection.drop_database(TestingConfig.MONGO_DB)

if __name__ == '__main__':
    unittest.main()
