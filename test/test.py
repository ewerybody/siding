'''
Created on 21.06.2018

@author: eric
'''
import os
import sys
import json
import uuid
import time
import unittest
import subprocess

import singlesiding


HERE = os.path.dirname(os.path.abspath(__file__))
print('HERE: %s' % HERE)
TEST_APP_PATH = os.path.join(HERE, 'app_test_app.py')


class Test(unittest.TestCase):

    def test_app(self):
        print('test_app ...')
        p = subprocess.run([sys.executable, TEST_APP_PATH])
        print('p: %s' % p)
#        app = singlesiding.initialize('test', 'test app', '1')
#        app.message_received.connect()
#        app = QSingleApplication()
#        app.setOrganizationName()
#        app.setApplicationName()
#        app.setApplicationVersion("1")
#        app.ensure_single()

    def test_app2(self):
        print('test_app2 ...')
        p = subprocess.run([sys.executable, TEST_APP_PATH])
        print('p: %s' % p)


if __name__ == '__main__':
    unittest.main(verbosity=2)
