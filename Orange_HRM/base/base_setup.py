from selenium import webdriver
from Orange_HRM.base import browser_setup

class BaseSetup(object):

    def setUp(self):
        if browser_setup['browser'] == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_setup['browser'] == 'chrome':
            self.driver = webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        else:
            raise Exception("Not supported browser!")

        self.driver.maximize_window()

        self.driver.get(browser_setup['url'])

    def tearDown(self):

        self.driver.quit()
