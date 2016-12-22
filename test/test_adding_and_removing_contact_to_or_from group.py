from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

'''Реализовать тесты для добавления контакта в группу и удаления контакта из группы.

Все действия выполнять через пользовательский интерфейс, а при проверках использовать информацию, загружаемую из базы данных напрямую.

Не забывайте про обеспечение выполнения предусловий.


def test_adding_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:  # создаем группу, если не существует
        app.group.create(Group(name="group"))
    if len(db.get_contact_list()) == 0:  # создаем контакт , если не существует
        app.contact.create_contact(Contact(firstname_of_contact="Contact added"))
    groups = db.get_group_list()  # получаем список групп из бд
    group = random.choice(groups)  # берем группу в которую будем добавлять контакты
    contacts = db.get_contact_list()  # получаем список контактов из бд
    contact_for_adding = random.choice(contacts)  # получаем контакт, кот. будем добавлять
    contacts_in_group_before_adding = data_base.get_contacts_in_group(
        Group(id=group.id))  # получаем список контактов выбраной группы
    if contact_for_adding not in contacts_in_group_before_adding:  # если контакт не в списке контактов выбранной группы, добавляем его туда
        app.contact.add_contact_to_group(contact_for_adding.id, group.id)
        contacts_in_group_after_adding = data_base.get_contacts_in_group(
            Group(id=group.id))  # получаем список контактов выбраной группы после добавления контакта
        assert len(contacts_in_group_before_adding) + 1 == len(contacts_in_group_after_adding)
        assert contact_for_adding in contacts_in_group_after_adding
    else:
        print("The contact is already there")





'''


def test_removing_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:  # создаем группу, если не существует
        app.group.create(Group(name="group"))
    if len(db.get_contact_list()) == 0:  # создаем контакт , если не существует
        app.contact.create_contact(Contact(firstname_of_contact="Contact added"))
    groups = db.get_group_list()  # получаем список групп из бд
    group = random.choice(groups)  # берем группу из которой  будем удалять контакты
    contacts = db.get_contact_list()  # получаем список контактов из бд
    contact_for_removing = random.choice(contacts)  # получаем контакт, кот. будем удалять
    contacts_in_group_before_removing = data_base.get_contacts_in_group(
        Group(id=group.id))  # получаем список контактов выбраной группы до удаления
    if contact_for_removing in contacts_in_group_before_removing:  # если контакт  в списке контактов выбранной группы, удаляем его  оттуда
        app.contact.remove_contact_from_group(contact_for_removing.id, group.id)
        contacts_in_group_after_removing = data_base.get_contacts_in_group(Group(id=group.id))  # получаем список контактов выбраной группы после удаления контакта
        assert len(contacts_in_group_before_removing) == len(contacts_in_group_after_removing) - 1
        assert contact_for_removing not in contacts_in_group_after_removing
    else:
        print("The contact is already removed")
