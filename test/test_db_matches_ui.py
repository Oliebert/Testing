from model.group import Group
from timeit import timeit# время загрузки бд через пользовательский интерфейс и через db mysql
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    #print(timeit(lambda: app.group.get_group_list(), number=1)) # вместо того чтобы сохранять списки, делаем лямбда функцию, измеряем время один раз
    def clean (group):
        return Group(id = group.id, name=group.name.strip())# удаление пробелов в начале и в конце
    #print(timeit(lambda:map(clean, db.get_group_list()), number= 1000))
    db_list = map(clean, db.get_group_list())
    #assert False #для упавших тестов информация выводится на консоль
    assert sorted(ui_list, key =Group.id_or_max) == sorted(db_list, key =Group.id_or_max)
        # в бд сохраняются лишние пробелы, а в ui эти пробелы убираются

'''Переделать тесты для проверки информации о контактах на главной странице -- на этот раз нужно реализовать сравнение для всех записей,
а не для одной случайно выбранной. А сравнивать -- с информацией, загруженной из базы данных.'''

def test_match_contacts_with_db(app, db):
   contacts_list_from_db = sorted(db.get_contact_list(),key=Contact.id_or_max)
   contacts_list_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
   assert contacts_list_from_db == contacts_list_from_ui
