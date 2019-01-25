# coding:utf-8
import time
from selenium import webdriver
from test1.basepage import BasePage


class BaiduSearch(object):
    driver_path = '/Users/juu/PycharmProjects/automation_framework_demo/myself/chromedriver'
    driver = webdriver.Chrome(driver_path)

    bp = BasePage(driver)


    def open_baidu(self):
        self.bp.open_url('https://www.baidu.com')
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.bp.quit_browser()


if __name__ == "__main__":
    baidu = BaiduSearch()
    baidu.open_baidu()
    baidu.test_search()