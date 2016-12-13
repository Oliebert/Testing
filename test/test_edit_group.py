from model.group import Group
from random import randrange
import random

def test_edit_group_name(app, db, check_ui):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="New_group")) # erstellen wir eine Gruppe

    old_groups = db.get_group_list() # Liste der Gruppen bevors Hinzufügen einer neuen Gruppe

   # index = randrange(len(old_groups))

    group = random.choice(old_groups)

    old_groups.remove(group)

    edit_group = Group(name="Edit_group")

    edit_group.id = group.id          # eine id von der alte gruppe behalten wir bei

    old_groups.append(edit_group)

    app.group.edit_group_by_id(group.id, edit_group)

    new_groups = db.get_group_list()

    #assert len(old_groups) == len(new_groups)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
'''

def test_edit_group_footer(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe

    old_groups = app.group.get_group_list()



    app.group.edit_first_group(Group(footer="header_name_changed"))

    new_groups = app.group.get_group_list()

    assert len(old_groups)  == len(new_groups)

'''