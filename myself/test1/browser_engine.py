# coding: utf-8
from selenium import webdriver
from time import sleep

class BrowserEngine(object):
    """
    定义浏览器驱动
    """
    chrome_path = '/Users/juu/PycharmProjects/automation_framework_demo/myself/chromedriver'
    fire_path = '/Users/juu/PycharmProjects/automation_framework_demo/myself/geckodriver'


    def __init__(self, browser_type):
        self.browser_type = browser_type

    def get_browser(self):
        if self.browser_type == 'Chrome':
            driver = webdriver.Chrome(executable_path=self.chrome_path)
        elif self.browser_type == 'Firefox':
            driver = webdriver.Firefox(executable_path=self.fire_path)
        elif self.browser_type == 'IE':
            driver = webdriver.Ie(executable_path=self.chrome_path)
        else:
            driver = webdriver.Chrome(executable_path=self.chrome_path)

        driver.maximize_window()
        driver.implicitly_wait(3)

        return driver



if __name__ == '__main__':
    browser_engine = BrowserEngine('Firefox')
    browser_engine.get_browser()
    sleep(3)

