import re
from model.contact import Contact

def test_match_with_db(app, db):
    contacts_from_db = sorted(db.get_contact_list(),key=Contact.id_or_max)  #
    phones_from_db = db.phones_from_db()
    email_list_from_db = db.emails_from_db()
    phone_list_db= []
    for phone in phones_from_db:
        phone_list_db.append(merge_phones_like_on_home_page(phone))
    email_list_db = []
    for email in email_list_from_db:
        email_list_db.append(merge_mail_like_on_home_page(email))

    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
                                                                           # phones_from_ui = []
    phones_from_ui = [contact.all_phones for contact in contacts_from_ui]  # for contact in contacts_from_ui :
                                                                           #          phones_from_ui.append(contact.all_phones)

    emails_from_ui = [contact.all_emails for contact in contacts_from_ui]

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