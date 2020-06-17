from Orange_HRM.base import browser_setup,base_setup
from selenium.webdriver.common.by import By
from Orange_HRM.base import webdriver_custom

class Login_Page:

    def __init__(self,base_setup,webdriver_custom):
        username_field = (By.ID, 'txtUsername')
        _password_field = (By.ID, 'txtPassword')
        _login_button = (By.ID, 'btnLogin')
        _welcome_button = (By.ID, 'welcome')

    def username_send_keys(self, data=''):
        self.send_keys_to(self.username_field, data)

    def password_send_keys(self, data=''):
        self.send_keys_to(self._password_field, data)

    # def fill_login_form(self, username, password):
    #     #
    #     #     self.find_element(self.username_field).send_keys(username)
    #     #     self.find_element(self._password_field).send_keys(password)
    #     #     # self.find_element(self._login_button).click()


