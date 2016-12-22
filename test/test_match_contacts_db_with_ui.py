import re
from model.contact import Contact

'''Переделать тесты для проверки информации о контактах на главной странице -- на этот раз нужно реализовать сравнение для всех записей,
а не для одной случайно выбранной. А сравнивать -- с информацией, загруженной из базы данных.'''


def test_match_with_db(app, db):
    contacts_from_db = sorted(db.get_contact_list(),key=Contact.id_or_max) # получаем сортированный список контактов из дб
    phones_from_db = db.phones_from_db()      # получаем  список телефонов из дб
    email_list_from_db = db.emails_from_db()  #-- список емэйлов из дб

    phone_list_db = []                        # определяем пустой список для добавления телефонов из дб

    for phone in phones_from_db:

        phone_list_db.append(merge_phones_like_on_home_page(phone))   # в пустой список добавляем, убирая пробелы, телефоны

    email_list_db = []                        # определяем пустой список для добавления телефонов

    for email in email_list_from_db:

        email_list_db.append(merge_mail_like_on_home_page(email))     # в пустой список добавляем, убирая пробелы, емэйлы

    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max) # получаем сортированный список контактов из ui

    phones_from_ui = []                               # определяем пустой список для добавления телефонов из ui
    for con in contacts_from_ui:
         phones_from_ui.append(con.all_phones)

    #phones_from_ui = [con.all_phones for con in contacts_from_ui]

    emails_from_ui = [con.all_emails for con in contacts_from_ui]

    assert contacts_from_db == contacts_from_ui

    assert phone_list_db == phones_from_ui

    assert email_list_db == emails_from_ui


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homenumber, contact.mobilenumber, contact.worknumber, contact.contact_phone2]))))


def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.contact_email, contact.contact_email2, contact.contact_email3])))