from selenium import webdriver    #.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper

class Application:

    def __init__(self, browser, base_url):

        if browser == "firefox":
            self.wd = webdriver.Firefox()#firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s " % browser)

        self.session = SessionHelper(self)

        self.base_url = base_url
                                                    #driver wird ein einziges Mal inizilisiert bei der Erschaffung einer Fixture.
                                                    #ein Helper übernimmt einen Link auf ein Objekt der Klasse Application
                                                    #was uns die Möglichkeit gibt über einen Helper uns zu anderem wenden
        self.group = GroupHelper(self)

        self.contact = ContactHelper(self)

  #      self.navigation = NavigationHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url                     #URL of the current loaded page
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()