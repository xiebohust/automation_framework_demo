from time import sleep
import unittest
import paramunittest
from common import common
from common.common import Element
from common.Log import MyLog as Log
import readConfig as readConfig

login_xls = common.get_xls("shein", "www", "testCase.xls", "login")
localReadConfig = readConfig.ReadConfig()


@paramunittest.parametrized(*login_xls)
class TestLogin(unittest.TestCase):

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
        return self.case_name

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
        if Element("shein", "www", "login", "login_link").is_exist():
            Element("shein", "www", "login", "login_link").click()

        # find email and password and input value
        Element("shein", "www", "login", "email").send_key(self.email)
        sleep(1)
        Element("shein", "www", "login", "password").send_key(self.password)
        sleep(1)
        Element("shein", "www", "login", "login_bt").get_element_by_index(0).click()
        sleep(1)

        # print('%s' % ('login success!'))
        self.description()

    def check_result(self):
        """
        check result
        :return:
        """
        if self.result == '0':
            value = self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div[3]/div[1]/a/span')[0].get_attribute('text')
            self.assertEqual(value, self.email.split('@')[0])
            # print('%s' % ('OK.'))
        if self.result == '1':
            value = Element("shein", "www", "login", "login_error").getAttribute()
            self.assertEqual(value, 'The Email Address or Password you entered is incorrect.')

    def tearDown(self):
        """
        after test
        :return:
        """
        self.log.build_end_line(self.case_name)


