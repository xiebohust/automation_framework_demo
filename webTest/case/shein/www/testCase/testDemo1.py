from time import sleep
from selenium import webdriver
import unittest


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        # 窗口最大化
        self.driver.maximize_window()
        self.email = '1234@163.com'
        self.password = '123456'
        self.url = 'https://www.shein.com'

    def testLogin(self):
        """
        test body
        :return:
        """
        # open browser
        self.driver.get(self.url)
        sleep(3)
        # click login link
        self.driver.find_element_by_id('my_profile').click()
        sleep(1)

        # find email and password and input value
        self.driver.find_element_by_id('returning_email').send_keys(self.email)
        sleep(1)
        self.driver.find_element_by_id('returning_password').send_keys(self.password)
        sleep(1)
        self.driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div[3]/input[3]')[0].click()
        sleep(1)

        print('%s' % ('login success!'))
        self.checkResult()

        self.driver.close()

    def checkResult(self):
        """
        check result
        :return:
        """
        value = self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div/div/div/div[3]/div[1]/a/span')[0].get_attribute('text')
        self.assertEqual(value, 'Hi,1234 ')
        print('%s' % ('OK.'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

