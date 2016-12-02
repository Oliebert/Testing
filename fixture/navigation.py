from selenium import webdriver

class NavigationHelper:

    def __init__(self, app, browser, base_url):
        self.app = app
        self.base_url = base_url


    def open_home_page(self ):
        wd = self.app.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
