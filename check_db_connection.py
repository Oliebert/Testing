
import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database ="addressbook", user = "root", password="")

try: # для того чтобы выполнить запрос к базе данных, который создается при помощи метода connection

    cursor = connection.cursor()
    cursor.execute("select*from group_list")
    for row in cursor.fetchall(): # fetchall возвращает всю извлеченную информацию в виде набора строк
        print (row)

finally:
    connection.close()