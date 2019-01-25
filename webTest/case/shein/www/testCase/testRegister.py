import unittest
from time import sleep

import paramunittest

from comm import common
from comm.Log import MyLog as Log
from comm.common import Element

register_xls = common.get_xls("testCase.xls", "register")


@paramunittest.parametrized(*register_xls)
class TestRegister(unittest.TestCase):
    def setParameters(self, case_name, email, password, password_confirm, result):
        """
        :param case_name:
        :param email:
        :param password:
        :param password_confirm:
        :param result:
        :return:
        """
        self.case_name = str(case_name)
        self.email = str(email)
        self.password = str(password)
        self.password_confirm = str(password_confirm)
        self.result = str(result)
        print("setParameters!")

    def description(self):
        """

        :return:
        """
        self.case_name
        print("description!")

    def setUp(self):
        """
        before test
        :return:
        """
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.log.build_start_line(self.case_name)
        print("setUp!")

    def testRegister(self):
        """
        test body
        :return:
        """
        print("In testRegister!")
        try:
            if Element("register", "register_link").is_exist():
                Element("register", "register_link").click()

                # find email and password and input value
            Element("register", "email").send_key(self.email)
            sleep(1)
            if self.result == '1':
                value = Element("register", "email_error").get_text_value()
                self.assertEqual(value, "Your Email Address Incorrect!")

            Element("register", "password").send_key(self.password)
            sleep(1)
            Element("register", "password1").send_key(self.password_confirm)
            sleep(1)
            Element("register", "register_bt").get_element_by_index(0).click()
            sleep(1)

        except Exception as ex:
            self.logger.error(str(ex))

    def check_result(self):
        """
        check result
        :return:
        """
        print("In check result!")
        if self.result == '0':
            value = Element("register", "register_ok").get_text_value()
            self.assertEqual(value, "Congratulations! You have successfully registered!")
        if self.result == '1':
            value = Element("register", "email_error").get_text_value()
            self.assertEqual(value, "Please check your email format.")

    def tearDown(self):
        """
        after test
        :return:
        """
        self.log.build_end_line(self.case_name)
        print("tearDown!")
