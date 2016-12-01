# -*- coding: utf-8 -*-


from model.contact import Contact
import pytest
import random
import string # содержит константы хранящие списки символов

def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_letters + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную

testdata = [Contact(firstname_of_contact="", lastname_of_contact="")] + [
            Contact(firstname_of_contact=random_string("firstname", 10), lastname_of_contact=random_string("lastname", 10))
            for i in range(5)]

@pytest.mark.parametrize("contact" ,  testdata, ids = [repr(a) for a in testdata] )  # ids- список с текстовым представлением данных (преобразование в строки )

def test_add_contact(app, contact):

    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()

    new_contacts = app.contact.get_contact_list()

    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

'''
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

