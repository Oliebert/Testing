# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

from model.contact import Contact


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_contact(app):



    app.session.login( username="admin", password="secret")


    app.contact.create_contact(Contact(firstname_of_contact="nknnn", middlename_of_contact="khknkhn",
                                        lastname_of_contact="khknkhn", contactnickname="kbjb",

                                        contacttittle="jbjbjhbb", contactcompany="lkmllnm", contactaddress="knkhnkhnkn",
                                        homenumber="nkjjhj", mobilenumber="nknknk",

                                        worknumber="ihihkh", contact_email="knkjnb", contact_fax="lmkl",
                                        contact_notes="bjbjb", contact_email2="jljljj",

                                        contact_email3="jbjb", contact_homepage="nknjn", contact_address2="jjhbknb",
                                        contact_phone2="bbjb"))

    app.session.logout()


def test_empty_contact(app):



    app.session.login( username="admin", password="secret")


    app.contact.create_contact( Contact(firstname_of_contact="", middlename_of_contact="",
                                        lastname_of_contact="", contactnickname="",

                                        contacttittle="", contactcompany="", contactaddress="",
                                        homenumber="", mobilenumber="",

                                        worknumber="", contact_email="", contact_fax="", contact_notes="",
                                        contact_email2="",

                                        contact_email3="", contact_homepage="", contact_address2="",
                                        contact_phone2=""))

    app.session.logout()





