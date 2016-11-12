from model.group import Group

def test_edit_first_group(app):

    app.session.login(username="admin", password="secret")

    app.group.edit_group(Group(name="group_name_changed", header="header_name_changed", footer="footer_name_changed"))

    app.session.logout()