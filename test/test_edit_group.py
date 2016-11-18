from model.group import Group

def test_edit_group_name(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe


    app.group.edit_first_group(Group(name="group_name_changed"))



def test_edit_group_header(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe

    app.group.edit_first_group(Group(header="header_name_changed"))



def test_edit_group_footer(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe


    app.group.edit_first_group(Group(footer="header_name_changed"))

