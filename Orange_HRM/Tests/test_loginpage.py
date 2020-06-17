from Orange_HRM.base import browser_setup,base_setup
from Orange_HRM.Pages.LoginPage import Login_Page
# import unittest
import pytest

class test_loginPage(base_setup):

    def setUp(self):
        super(test_loginPage, self).setUp()
        self.Pages = Login_Page(self.driver,self.get_by_type)

        def test_Log_in(self):
            self.Pages.username_send_keys(data='')


        def tearDown(self):
            super(test_loginPage, self).tearDown()
            self.driver.quit()

if __name__ == '__main__':
    pytest.main()
