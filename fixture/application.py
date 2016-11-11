from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()#firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

                                                    #driver wird ein einziges Mal inizilisiert bei der Erschaffung einer Fixture.
                                                    #ein Helper übernimmt einen Link auf ein Objekt der Klasse Application
                                                    #was uns die Möglichkeit gibt über einen Helper uns zu anderem wenden
        self.group = GroupHelper(self)

        self.contact = ContactHelper(self)

        self.navigation = NavigationHelper(self)



    def destroy(self):
        self.wd.quit()