
from model.contact import Contact


def test_edit_contact(app):

    app.session.login(username="admin", password="secret")

    app.contact.edit_contact(Contact(firstname_of_contact="firstname_changed", middlename_of_contact="middlename_changed",
                                        lastname_of_contact="lastname_changed", contactnickname="contactnickname_changed",

                                        contacttittle="contacttittle_changed", contactcompany="contactcompany_changed", contactaddress="contactaddress_changed",
                                        homenumber="homenumber_changed", mobilenumber="mobilenumber_changed",

                                        worknumber="worknumber_changed", contact_email="contact_email_changed", contact_fax="contact_fax_changed",
                                        contact_notes="contact_notes_changed", contact_email2="contact_email2_changed",

                                        contact_email3="contact_email3_changed", contact_homepage="contact_homepage_changed", contact_address2="contact_address2_changed",
                                        contact_phone2="contact_phone2_changed"))

    app.session.logout()