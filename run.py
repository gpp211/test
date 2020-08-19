import unittest
from common import HTMLTestRunnerNew
import time

testsuite = unittest.TestSuite()
suite = unittest.defaultTestLoader.discover('./test_cases')
testsuite.addTests(suite)
currenttime = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = r'report/reporter.html'
with open(filename, 'wb+') as f:
    HTMLTestRunnerNew.HTMLTestRunner(stream=f,
                                     title='学生管理系统',
                                     description='balala',
                                     tester='xml').run(testsuite)