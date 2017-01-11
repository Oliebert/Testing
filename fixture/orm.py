
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
'''Object Relational Mapping-инструмент, помогающий установить отношение между классами, написанными на языке программирования и таблицами базы данных'''


class ORMFixture:

    db = Database() #объект на основании которого мы будем строить привязку

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)  # привязка  к бд
        self.db.generate_mapping()  # сопоставление описанных классов со свойствами таблиц
        sql_debug(True)

    class ORMGroup(db.Entity): # привязка описывается набором класса. описываем набор свойств и привязываем их к таблице
        _table_= 'group_list'
        id = PrimaryKey(int, column='group_id')# int- тип поля в базе данных, переменные не совпадают с названием столбцов где они хранятся, поэтому добавляем column
        name = Optional(str, column='group_name')#
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table ="address_in_groups", column="id", reverse="groups", lazy=True  ) #Set - множество

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')  # int- тип поля в базе данных, переменные не совпадают с названием столбцов где они хранятся, поэтому добавляем column
        firstname = Optional(str, column='firstname')  #
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime,column='deprecated')
        groups = Set(lambda:ORMFixture.ORMGroup, table ="address_in_groups", column="group_id", reverse="contacts", lazy=True )

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

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]# извлекаем группу с заданным идентификатором, первый объект
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]# извлекаем группу с заданным идентификатором, первый объект
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups ))




