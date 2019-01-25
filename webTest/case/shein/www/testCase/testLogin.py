import unittest
from time import sleep
import paramunittest
from comm import common
from comm.common import Element
from comm.Log import MyLog as Log

login_xls = common.get_xls("testCase.xls", "login")


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):

    def setParameters(self, case_name, email, password, result):
        """
        set parameters
        :param case_name:
        :param email:
        :param password:
        :param result:
        :return:
        """
        self.case_name = str(case_name)
        self.email = str(email)
        self.password = str(password)
        self.result = str(result)

    def description(self):
        """
        case description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        before test
        :return:
        """
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.log.build_start_line(self.case_name)

    def testLogin(self):
        """
        test body
        :return:
        """
        if Element("login", "login_link").is_exist():
            Element("login", "login_link").click()

        # find email and password and input value
        Element("login", "email").send_key(self.email)
        sleep(1)
        Element("login", "password").send_key(self.password)
        sleep(1)
        Element("login", "login_bt").get_element_by_index(0).click()
        sleep(1)

        # print('%s' % ('login success!'))
        self.check_result()

    def check_result(self):
        """
        check result
        :return:
        """
        if self.result == '0':
            value = Element("login", "login_ok").get_text_value()
            self.assertEqual(value, "Hi,"+self.email.split('@')[0])
            # print('%s' % ('OK.'))
        if self.result == '1':
            value = Element("login", "login_error").get_text_value()
            self.assertEqual(value, 'The Email Address or Password you entered is incorrect.')

    def tearDown(self):
        """
        after test
        :return:
        """
        Element("logout", "logout_link").click()
        sleep(1)
        self.log.build_end_line(self.case_name)


