from model.group import Group
from timeit import timeit# время загрузки бд через пользовательский интерфейс и через db mysql


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1)) # вместо того чтобы сохранять списки, делаем лямбда функцию, измеряем время один раз
    def clean (group):
        return Group(id = group.id, name=group.name.strip())# удаление пробелов в начале и в конце
    print(timeit(lambda:map(clean, db.get_group_list()), number= 1000))

    assert False #для упавших тестов информация выводится на консоль
        #sorted(ui_list, key =Group.id_or_max) == sorted (db_list, key =Group.id_or_max)
        # в бд сохраняются лишние пробелы, а в ui эти пробелы убираются