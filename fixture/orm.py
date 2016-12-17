
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:

    db = Database() #объект на основании которого мы будем строить привязку

    class ORMGroup(db.Entity): # привязка описывается набором класса. описываем набор свойств и привязываем их к таблице
        _table_= 'group_list'
        id = PrimaryKey(int, column='group_id')# int- тип поля в базе данных, переменные не совпадают с названием столбцов где они хранятся, поэтому добавляем column
        name = Optional(str, column='group_name')#
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int,column='id')  # int- тип поля в базе данных, переменные не совпадают с названием столбцов где они хранятся, поэтому добавляем column
        firstname = Optional(str, column='firstname')  #
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime,column='deprecated')

    def __init__(self,host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)# привязка  к бд
        self.db.generate_mapping() # сопоставление описанных классов со свойствами таблиц
        sql_debug(True)

    def convert_groups_to_model(self, groups):# преобразуем полученные объекты ORM в объекты, описанные в нашей model
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer )
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):# преобразуем полученные объекты ORM в объекты, описанные в нашей model
        def convert(contact):
            return Contact(id=str(contact.id), firstname_of_contact=contact.firstname, lastname_of_contact=contact.lastname )
        return list(map(convert, contacts))

    # реализуем функции, которые получают списки объектов
    @db_session # запросы выполняются в рамках сессии
    def get_group_list(self): # sql запросы генерируются автоматически
        #with db_session:
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))# запрос превращаем в список(list)

    @db_session  # запросы выполняются в рамках сессии
    def get_contact_list(self):  # sql запросы генерируются автоматически
        # with db_session:
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))  # запрос превращаем в список(list)



