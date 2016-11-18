from model.contact import Contact

def test_delete_contact(app):

    if app.contact.count_contact() == 0: # falls keinen Contact gibt´s

        app.contact.create_contact(Contact(firstname_of_contact="test_firstname", mobilenumber="test_mo")) # erstellen wir einen Contact

    app.contact.delete_first_contact()

