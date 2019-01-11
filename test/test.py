'''
Created on 21.06.2018

@author: eric
'''
import os
import sys
import time
import unittest
import subprocess

# we cannot test QSingleApplication here directly because we'd need
# to app.exec_() the thing and thus halt the process.
# import singlesiding


HERE = os.path.dirname(os.path.abspath(__file__))
TEST_APP_PATH = os.path.join(HERE, 'app_test_app.py')


class Test(unittest.TestCase):

    def test_app(self):
        p1 = subprocess.Popen([sys.executable, TEST_APP_PATH])
        time.sleep(0.2)
        self.assertTrue(_is_running(p1.pid))
        print('p1.pid: %s' % p1.pid)
        # process 1 is onening

        p2 = subprocess.Popen([sys.executable, TEST_APP_PATH])
        print('p2.pid: %s' % p2.pid)
        p2.wait(5)
        self.assertFalse(_is_running(p2.pid))
        # process 2 killed itself

        p1.terminate()
        time.sleep(0.2)
        self.assertFalse(_is_running(p1.pid))
        # process 1 was terminated


def _is_running(pid):
    cmd = 'wmic.exe process where processID="%s" get name /format:list' % pid
    output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).strip()
    if not isinstance(output, str):
        output = output.decode()
    return output != ''


if __name__ == '__main__':
    unittest.main(verbosity=2)
