from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
from application import Application

import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_test_add_group(self):


        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page()
        self.app.group_creation( Group(name="knlnölnlmlml", header="GUBJHB", footer="lknlknkln"))
        self.app.return_to_group()
        self.app.logout()


    def test__add_empty_group(self):


        self.app.open_home_page()
        self.app.login( username="admin", password="secret")
        self.app.open_groups_page()
        self.app.group_creation( Group(name="", header="", footer=""))
        self.app.return_to_group()
        self.app.logout()



    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()