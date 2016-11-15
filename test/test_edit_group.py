from model.group import Group

def test_edit_group_name(app):


    app.group.edit_first_group(Group(name="group_name_changed"))



def test_edit_group_header(app):

    app.group.edit_first_group(Group(header="header_name_changed"))



def test_edit_group_footer(app):

    app.group.edit_first_group(Group(footer="header_name_changed"))

