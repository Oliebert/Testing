from model.group import Group

def test_delete_first_group(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe

    app.group.delete_first_group()

