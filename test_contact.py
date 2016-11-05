# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from applcation_for_contact import Application_For_Contact
import unittest
from contact import Contact


@pytest.fixture

def app(request):
    fixture = Application_For_Contact()
    request.addfinalizer(fixture.destroy)
    return fixture





def test_contact(self):
    # success = True

    self.app.open_home_page()
    self.app.login( username="admin", password="secret")

    self.app.open_contact_page()
    self.app.create_contact( Contact(firstname_of_contact="nknnn", middlename_of_contact="khknkhn", lastname_of_contact="khknkhn", contactnickname="kbjb",

                            contacttittle="jbjbjhbb", contactcompany="lkmllnm", contactaddress="knkhnkhnkn", homenumber="nkjjhj", mobilenumber="nknknk",

                            worknumber="ihihkh", contact_email="knkjnb", contact_fax="lmkl", contact_notes="bjbjb", contact_email2="jljljj",

                            contact_email3="jbjb", contact_homepage="nknjn", contact_address2="jjhbknb", contact_phone2="bbjb"))

    self.app.logout()
        #self.assertTrue(success)

def test_empty_contact(self):
    success = True

    self.app.open_home_page()
    self.app.login( username="admin", password="secret")

    self.app.open_contact_page()
    self.app.create_contact( Contact(firstname_of_contact="", middlename_of_contact="",
                            lastname_of_contact="", contactnickname="",

                            contacttittle="", contactcompany="", contactaddress="",
                            homenumber="", mobilenumber="",

                            worknumber="", contact_email="", contact_fax="", contact_notes="",
                            contact_email2="",

                            contact_email3="", contact_homepage="", contact_address2="",
                            contact_phone2=""))

    self.app.logout()
    self.assertTrue(success)


    def tearDown(self):
        self.app.destroy()
