# coding:utf-8

from selenium import webdriver


class BasePage(object):
    """封装方法
    back()
    forward()
    get()
    quit()"""

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    driver_path = '/Users/juu/PycharmProjects/automation_framework_demo/myself/chromedriver'
    driver = webdriver.Chrome(driver_path)
    bp = BasePage(driver)
    bp.open_url('https://www.baidu.com')