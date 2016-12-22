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
    wd.get("http://localhost/addressbook/?group=427")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    if not wd.find_element_by_xpath("//form[@id='right']/select//option[4]").is_selected():
        wd.find_element_by_xpath("//form[@id='right']/select//option[4]").click()
    if not wd.find_element_by_xpath("//input[@id='489']").is_selected():
        wd.find_element_by_xpath("//input[@id='489']").click()
    wd.find_element_by_name("remove").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
