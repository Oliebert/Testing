from model.group import Group

def test_edit_group_name(app):

    app.session.login(username="admin", password="secret")

    app.group.edit_first_group(Group(name="group_name_changed"))

    app.session.logout()


def test_edit_group_header(app):

    app.session.login(username="admin", password="secret")

    app.group.edit_first_group(Group(header="header_name_changed"))

    app.session.logout()


def test_edit_group_footer(app):

    app.session.login(username="admin", password="secret")

    app.group.edit_first_group(Group(footer="header_name_changed"))

    app.session.logout()