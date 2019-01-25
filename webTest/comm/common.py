import os
import readConfig as readConfig
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from comm.webDriver import MyDriver as Driver
import time
import comm.runSet as runSet

localReadConfig = readConfig.ReadConfig()


def open_browser():
    """
    open browser by url
    :return:
    """
    browser = webdriver.Chrome()
    # 窗口最大化
    browser.maximize_window()
    return browser


def close_browser(browser):
    """
    close browser
    :param browser:
    :return:
    """
    browser.close()


def open_url(name):
    """
    open web page by url
    :param name:
    :return:
    """
    url = localReadConfig.get_webServer(name)
    browser = open_browser()
    browser.get(url)
    return browser


def get_xls(xls_name, sheet_name):
    """

    :param xls_name: excel file name
    :param sheet_name: sheet name
    :return: sheet value
    """
    web = runSet.get_web()
    site = runSet.get_site()
    cls = []
    # get excel file path
    xls_path = os.path.join(readConfig.proDir, 'file', web, site, xls_name)
    print("xls path:"+xls_path)

    # open excel file
    book = open_workbook(xls_path)
    # get sheet by name
    sheet = book.sheet_by_name(sheet_name)
    # get nrows
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
            # print(sheet.row_values(i))
    return cls

activity = {}


def set_xml():
    """
    get element
    :return:
    """
    web = runSet.get_web()
    site = runSet.get_site()
    if len(activity) == 0:
        file_path = os.path.join(readConfig.proDir, 'file', web, site, 'element.xml')
        tree = ElementTree.parse(file_path)
        for a in tree.findall('activity'):
            activity_name = a.get('name')

            element = {}
            for e in a.getchildren():
                element_name = e.get('id')

                element_child = {}
                for t in e.getchildren():
                    element_child[t.tag] = t.text
                element[element_name] = element_child
            activity[activity_name] = element


def get_el_dict(activity_name, element):
    """
    According to page, activity and element getting element
    :param activity_name: activity name
    :param element: element name
    :return:
    """
    set_xml()
    element_dict = activity.get(activity_name).get(element)
    print(element_dict)
    return element_dict


class Element:

    def __init__(self, activity_name, element_name):

        self.driver1 = Driver.get_browser()
        self.driver = self.driver1.get_driver()
        self.activity = activity_name
        self.element = element_name
        element_dict = get_el_dict(self.activity, self.element)
        self.pathType = element_dict.get('pathType')
        self.pathValue = element_dict.get('pathValue')

    def is_exist(self):
        """
        Determine element is exist
        :return: TRUE OR FALSE
        """
        try:
            if self.pathType == 'ID':
                self.driver.find_element_by_id(self.pathValue)
                return True
            if self.pathType == 'XPATH':
                self.driver.find_elements_by_xpath(self.pathValue)
                return True
            if self.pathType == 'CLASSNAME':
                self.driver.find_element_by_class_name(self.pathValue)
                return True
            if self.pathType == 'NAME':
                self.driver.find_element_by_name(self.pathValue)
                return True
        except NoSuchElementException:
            return False

    def wait_element(self, wait_time):
        """
        wait element appear in time
        :param wait_time: wait time
        :return: true or false
        """
        time.sleep(wait_time)
        if self.is_exist():
            return True
        else:
            return False

    def get_element(self):
        """
        get element
        :return: element
        """
        try:
            if self.pathType == 'ID':
                element = self.driver.find_element_by_id(self.pathValue)
                return element
            if self.pathType == 'XPATH':
                element = self.driver.find_elements_by_xpath(self.pathValue)
                return element
            if self.pathType == 'CLASSNAME':
                element = self.driver.find_element_by_class_name(self.pathValue)
                return element
            if self.pathType == 'NAME':
                element = self.driver.find_element_by_name(self.pathValue)
                return element
        except NoSuchElementException:
            return None

    def get_element_by_index(self, index):
        """
        get element by index
        :param index: index
        :return: element
        """
        try:
            if self.pathType == 'ID':
                element = self.driver.find_element_by_id(self.pathValue)
                return element[index]
            if self.pathType == 'XPATH':
                element = self.driver.find_elements_by_xpath(self.pathValue)
                return element[index]
            if self.pathType == 'CLASSNAME':
                element = self.driver.find_element_by_class_name(self.pathValue)
                return element[index]
            if self.pathType == 'NAME':
                element = self.driver.find_element_by_name(self.pathValue)
                return element[index]
        except NoSuchElementException:
            return None

    def get_element_list(self):
        """
        get element list
        :return: element list
        """
        try:
            if self.pathType == 'ID':
                element_list = self.driver.find_element_by_id(self.pathValue)
                return element_list
            if self.pathType == 'XPATH':
                element_list = self.driver.find_elements_by_xpath(self.pathValue)
                return element_list
            if self.pathType == 'CLASSNAME':
                element_list = self.driver.find_element_by_class_name(self.pathValue)
                return element_list
            if self.pathType == 'NAME':
                element_list = self.driver.find_element_by_name(self.pathValue)
                return element_list
        except NoSuchElementException:
            return None

    def click(self):
        """
        click element
        :return:
        """
        element = self.get_element()
        time.sleep(1)
        element.click()

    def send_key(self, key):
        """
        input key
        :param key: input value
        :return:
        """
        element = self.get_element()
        time.sleep(1)
        element.clear()
        element.send_keys(key)

    def input_keys(self, index, key):
        """
        By index send key
        :param index: index
        :param key: key
        :return:
        """
        element = self.get_element_by_index(index)
        time.sleep(1)
        element.clear()
        element.send_keys(key)

    def get_text_value(self):
        """
        get attribute
        :return:
        """
        element = self.get_element()
        value = element.get_attribute('text')
        return str(value)
