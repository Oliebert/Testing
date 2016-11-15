# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

from model.contact import Contact

def test_add_contact(app):

   app.contact.create_contact(Contact(firstname_of_contact="nknnn", middlename_of_contact="khknkhn",
                                        lastname_of_contact="khknkhn", contactnickname="kbjb",

                                        contacttittle="jbjbjhbb", contactcompany="lkmllnm", contactaddress="knkhnkhnkn",
                                        homenumber="nkjjhj", mobilenumber="nknknk",

                                        worknumber="ihihkh", contact_email="knkjnb", contact_fax="lmkl",
                                        contact_notes="bjbjb", contact_email2="jljljj",

                                        contact_email3="jbjb", contact_homepage="nknjn", contact_address2="jjhbknb",
                                        contact_phone2="bbjb"))


def test_add_empty_contact(app):

    app.contact.create_contact( Contact(firstname_of_contact="", middlename_of_contact="",
                                        lastname_of_contact="", contactnickname="",

                                        contacttittle="", contactcompany="", contactaddress="",
                                        homenumber="", mobilenumber="",

                                        worknumber="", contact_email="", contact_fax="", contact_notes="",
                                        contact_email2="",

                                        contact_email3="", contact_homepage="", contact_address2="",
                                        contact_phone2=""))


