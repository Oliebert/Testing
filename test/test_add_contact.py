# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

from model.contact import Contact

def test_add_contact(app):

    old_contacts = app.contact.get_contact_list()

    contact = Contact(firstname_of_contact="nknnn", middlename_of_contact="khknkhn",
            lastname_of_contact="khknkhn", contactnickname="kbjb",

            contacttittle="jbjbjhbb", contactcompany="lkmllnm", contactaddress="knkhnkhnkn",
            homenumber="nkjjhj", mobilenumber="nknknk",

            worknumber="ihihkh", contact_email="knkjnb", contact_fax="lmkl",
            contact_notes="bjbjb", contact_email2="jljljj",

            contact_email3="jbjb", contact_homepage="nknjn", contact_address2="jjhbknb",
            contact_phone2="bbjb")

    app.contact.create_contact(contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

'''  def test_add_group(app):
        old_groups = app.group.get_group_list()

        group = Group(name="knlnölnlmlml", header="GUBJHB", footer="lknlknkln")

        app.group.create(group)

        new_groups = app.group.get_group_list()

        assert len(old_groups) + 1 == len(new_groups)

        old_groups.append(group)  # к новой группе присваивается самый большой идентификатор

        # assert old_groups == new_groups

def test_add_empty_contact(app):

    app.contact.create_contact(Contact(firstname_of_contact="", middlename_of_contact="",
                                        lastname_of_contact="", contactnickname="",

                                        contacttittle="", contactcompany="", contactaddress="",
                                        homenumber="", mobilenumber="",

                                        worknumber="", contact_email="", contact_fax="", contact_notes="",
                                        contact_email2="",

                                        contact_email3="", contact_homepage="", contact_address2="",
                                        contact_phone2=""))
'''

