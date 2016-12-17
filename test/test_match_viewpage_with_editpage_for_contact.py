# тест проверяет соответствует ли информация на главной странице той, что в форме редактирования
from random import randrange

import re


def test_all(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]                        # получаем список первого контакта
    contact_from_edit_page = app.contact.get_conact_info_from_edit_page(index)
    assert contact_from_home_page.homenumber == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.contact_email == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname_of_contact == contact_from_edit_page.firstname_of_contact
    assert contact_from_home_page.lastname_of_contact == contact_from_edit_page.lastname_of_contact
    assert contact_from_home_page.contactaddress == contact_from_edit_page.contactaddress.strip()


def clear(s):                                                                           # schneiden wir Sonderzeichen aus

    return re.sub("[() -]", "", s)                                                      # 1- welche Symbole , 2- welche wird es stattdessen sein , 3- wo

def merge_phones_like_on_home_page(contact): # функция склейки контактов в форме редактирования

    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.homenumber, contact.mobilenumber, contact.worknumber, contact.contact_phone2]))))# применяем функцию clear() ко всем элементам списка
                                                                                                                                  # с помощью первого filter оставляем только те строки, которые не пустые
                                                                                                                                  # c помощью второго filter выкидываем пустые значения None

def merge_emails_like_on_home_page(contact):

    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                [contact.contact_email, contact.contact_email2, contact.contact_email3])))