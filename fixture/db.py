import pymysql.cursors
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit=True  # кэширование работает и на чтение и на запись, кэш сбрасывается


    def get_group_list(self): # загружаем из базы данных список групп и контактов
        cursor = self.connection.cursor() # cursor - указатель не на обьект а на данные в базе
        try:
            list = []
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list") # запись на языке sql
            for row in cursor:
                (id, name, header, footer)= row # каждая из строк предствляет собой кортеж
                list.append(Group(id=str(id), name=name, header=header, footer=footer)) # в базе данных sql id представлено как число а в ui как строка

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
