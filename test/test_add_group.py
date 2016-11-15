
from model.group import Group

def test_add_group(app):

    app.group.create(Group(name="knlnölnlmlml", header="GUBJHB", footer="lknlknkln"))

    #app.session.logout()

def test_add_empty_group(app):

    app.group.create(Group(name="", header="", footer=""))








