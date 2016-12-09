
from model.group import Group
import random
import string # содержит константы хранящие списки символов

'''testdata = [Group(name="name1", header="header1", footer="footer1"),
            Group(name="name2", header="header2", footer="footer2")]
'''

def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_letters + string.digits #+ ""*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную

testdata = [ Group(name="", header="", footer="")] + [
            Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
             for i in range(5)]
