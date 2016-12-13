# метод извлекающий список контактов
import pymysql.cursors
from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name ="addressbook", user = "root", password="")

try: # для того чтобы выполнить запрос к базе данных, который создается при помощи метода connection
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))

    '''
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
    '''

    '''cursor = connection.cursor()
    cursor.execute("select*from group_list")
    for row in cursor.fetchall(): # fetchall возвращает всю извлеченную информацию в виде набора строк
        print (row)
    '''
finally:
    db.destroy()
    #connection.close()