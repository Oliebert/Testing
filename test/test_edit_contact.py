
from model.contact import Contact
from random import randrange

def test_edit_contact(app):

    if app.contact.count_contact() == 0: # falls keine Gruppe gibt´s

        app.contact.create_contact(Contact(firstname_of_contact="test_firstname", lastname_of_contact="lastname_changed", contactnickname="contactnickname_changed",))

    old_contacts = app.contact.get_contact_list()

    index = randrange(len(old_contacts))

    contact = Contact(firstname_of_contact="nk",
                      lastname_of_contact="kh",
                      contactnickname="kb",
                      contactcompany="lk", )

    contact.id = old_contacts[index].id

    app.contact.edit_contact_by_index(index, contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[index] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

'''def test_edit_empty_contact(app):

    if app.contact.count_contact() == 0:  # falls keine Gruppe gibt´s

        app.contact.create_contact(
            Contact(firstname_of_contact="", lastname_of_contact="",
                    contactnickname="", ))

        old_contacts = app.contact.get_contact_list()

        contact = Contact(firstname_of_contact="",
                          lastname_of_contact="",
                          contactnickname="",
                          contactcompany="", )

        contact.id = old_contacts[0].id

        app.contact.edit_first_contact(contact)

        new_contacts = app.contact.get_contact_list()

        assert len(old_contacts) == len(new_contacts)

        old_contacts[0] = contact

        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


  old_groups = app.group.get_group_list() # Liste der Gruppen bevors Hinzufügen einer neuen Gruppe

    group = Group(name="New_group")

    group.id = old_groups[0].id             # eine id von der alte gruppe behalten wir bei

    app.group.edit_first_group(group)

    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[0] = group

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# lastname wurde nicht geändert

def test_edit_firstname_of_contact(app):

    if app.contact.count_contact() == 0: # falls keine Gruppe gibt´s

        app.contact.create_contact(Contact(firstname_of_contact="test_firstname", mobilenumber="test_mo")) # erstellen wir eine Gruppe
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

'''