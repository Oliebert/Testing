from selenium.webdriver.firefox.webdriver import WebDriver

class Application_For_Contact:

    def __init__(self):
        self.wd = WebDriver(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()




    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
