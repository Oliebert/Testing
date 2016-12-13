from model.contact import Contact

from random import randrange
import random

def test_delete_contact(app, db, check_ui):

    if app.contact.count_contact() == 0: # falls keinen Contact gibt´s

        app.contact.create_contact(Contact(firstname_of_contact="test_firstname")) # erstellen wir einen Contact

    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)

    #index = randrange(len(old_contacts))

    app.contact.delete_contact_by_id(contact.id)

    #new_contacts = db.get_contact_list()

    assert len(old_contacts) - 1 == app.contact.count_contact()

    old_contacts.remove(contact)

    new_contacts = db.get_contact_list()

    assert sorted(old_contacts, key=Contact.id_or_max)== sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


   