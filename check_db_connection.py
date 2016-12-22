# метод извлекающий список контактов
import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name ="addressbook", user = "root", password="")

try: # для того чтобы выполнить запрос к базе данных, который создается при помощи метода connection
    l = db.get_contacts_in_group(Group(id="422"))
    for item in l:
        print(item)
    print(len(l))

    '''
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
    '''

    '''cursor = connection.cursor()
    cursor.execute("select*f rom group_list")
    for row in cursor.fetchall(): # fetchall возвращает всю извлеченную информацию в виде набора строк
        print (row)
    '''
finally:
    pass #db.destroy()
    #connection.close()