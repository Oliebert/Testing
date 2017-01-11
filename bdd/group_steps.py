from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group) #тестовые данные должны быть описаны там же где и тестовый сценарий



@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="some name"))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('a modify info with <name>, <header> and <footer>')
def modify_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I modify the group from the list')
def modify_group_from_the_list(app, random_group, modify_group):
    app.group.edit_group_by_id(random_group.id, modify_group)


@then('the new group list is equal to the old list with the modified group')
def verify_group_modified(db, non_empty_group_list, random_group, modify_group, app, check_ui):
    old_groups = non_empty_group_list
    new_group.id = random_group.id
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    old_groups.append(modify_group)
   #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(
            new_groups, key=Group.id_or_max) == sorted(app.group.get_contact_list(), key=Group.id_or_max)


