
from model.contact import Contact


'''def test_edit_contact(app):

     app.contact.edit_contact(Contact(firstname_of_contact="firstname_changed", middlename_of_contact="middlename_changed",
                                        lastname_of_contact="lastname_changed", contactnickname="contactnickname_changed",

                                        contacttittle="contacttittle_changed", contactcompany="contactcompany_changed", contactaddress="contactaddress_changed",
                                        homenumber="homenumber_changed", mobilenumber="mobilenumber_changed",

                                        worknumber="worknumber_changed", contact_email="contact_email_changed", contact_fax="contact_fax_changed",
                                        contact_notes="contact_notes_changed", contact_email2="contact_email2_changed",

                                        contact_email3="contact_email3_changed", contact_homepage="contact_homepage_changed", contact_address2="contact_address2_changed",
                                        contact_phone2="contact_phone2_changed"))

    app.session.logout()
'''
# lastname wurde nicht geändert

def test_edit_firstname_of_contact(app):
    app.contact.edit_first_contact(Contact(firstname_of_contact="firstname_changed"))


def test_edit_middlename_of_contact(app):
    app.contact.edit_first_contact(
        Contact(middlename_of_contact="middlename_changed"))

def test_edit_contactnickname(app):
    app.contact.edit_first_contact(
        Contact(contactnickname="contactnickname_changed"))

def test_edit_contacttittle(app):
    app.contact.edit_first_contact(
        Contact(contacttittle="contacttittle_changed"))

def test_edit_contactcompany(app):
    app.contact.edit_first_contact(
        Contact(contactcompany="contactcompany_changed"))

def test_edit_contactaddress(app):
    app.contact.edit_first_contact(
        Contact(contactaddress="contactaddress_changed"))

def test_edit_homenumber(app):
    app.contact.edit_first_contact(
        Contact(homenumber="homenumber_changed"))

def test_edit_mobilenumber(app):
    app.contact.edit_first_contact(
        Contact(mobilenumber="mobilenumber_changed"))

def test_edit_worknumber(app):
    app.contact.edit_first_contact(
        Contact(worknumber="worknumber_changed"))

def test_edit_contact_email(app):
    app.contact.edit_first_contact(
        Contact(contact_email="contact_email_changed"))

def test_contact_notes(app):
    app.contact.edit_first_contact(
        Contact(contact_notes="contact_notes_changed"))

def test_contact_email2(app):
    app.contact.edit_first_contact(
        Contact(contact_email2="contact_email2_changed"))

def test_contact_email3(app):
    app.contact.edit_first_contact(
        Contact(contact_email3="contact_email3_changed"))

def test_contact_homepage(app):
    app.contact.edit_first_contact(
        Contact(contact_homepage="contact_homepage_changed"))

def test_contact_address2(app):
    app.contact.edit_first_contact(
        Contact(contact_address2="contact_address2_changed"))

def test_contact_phone2(app):
    app.contact.edit_first_contact(
        Contact(contact_phone2="contact_phone2_changed"))
