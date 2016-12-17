# метод извлекающий список контактов
import pymysql.cursors
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name ="addressbook", user = "root", password="")

try: # для того чтобы выполнить запрос к базе данных, который создается при помощи метода connection
    l = db.get_contact_list()
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
    cursor.execute("select*from group_list")
    for row in cursor.fetchall(): # fetchall возвращает всю извлеченную информацию в виде набора строк
        print (row)
    '''
finally:
    pass #db.destroy()
    #connection.close()