from selenium import webdriver

class NavigationHelper:

    def __init__(self, app, browser, base_url):
        self.app = app
        self.base_url = base_url
        if browser == "firefox":
            self.wd = webdriver.Firefox()  # firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
