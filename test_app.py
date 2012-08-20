import os
from listener import application
from config import TestingConfig
import unittest
import json
from encoder import Encoder, Decoder
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
        pass

    def tearDown(self):
        pass

    def decode_status(self,resp):
        return json.loads(resp.data)['flag']

def tearDownModule():
    log.info('dropping database')

if __name__ == '__main__':
    unittest.main()
