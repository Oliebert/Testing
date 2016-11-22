from model.group import Group
from random import randrange

def test_edit_group_name(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="New_group")) # erstellen wir eine Gruppe

    old_groups = app.group.get_group_list() # Liste der Gruppen bevors Hinzufügen einer neuen Gruppe

    index = randrange(len(old_groups))

    group = Group(name="New_group")

    group.id = old_groups[index].id             # eine id von der alte gruppe behalten wir bei

    app.group.edit_group_by_index(index,group)

    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[index] = group

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''

def test_edit_group_footer(app):

    if app.group.count() == 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe

    old_groups = app.group.get_group_list()



    app.group.edit_first_group(Group(footer="header_name_changed"))

    new_groups = app.group.get_group_list()

    assert len(old_groups)  == len(new_groups)

'''