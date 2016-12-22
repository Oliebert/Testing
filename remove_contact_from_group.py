# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost/addressbook/group.php")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    wd.find_element_by_link_text("home").click()
    if not wd.find_element_by_xpath("//form[@id='right']/select//option[4]").is_selected():
        wd.find_element_by_xpath("//form[@id='right']/select//option[4]").click()
    if not wd.find_element_by_xpath("//input[@id='488']").is_selected():
        wd.find_element_by_xpath("//input[@id='488']").click()
    wd.find_element_by_xpath("//div[@id='content']/form[2]/div[3]/input").click()
    wd.find_element_by_xpath("//div[@class='msgbox']//a[.='group page \"nameRRK\"']").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
