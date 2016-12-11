from model.contact import Contact
import random
import string                                                              # содержит константы хранящие списки символов
import os.path
import jsonpickle
import getopt# для чтения опций из командной строки
import sys   # для того чтобы получить доступ к этим опциям

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])# n - количество генерируемых данных,
except getopt.GetoptError as err:                                                 # f- файл в который это все помещается
    # sys.argv это список параметров, которые переданы в программу из командной строки при запуске
    #1: это диапазон от второго элемента списка до последнего
    #почему от второго? потому что первый элемент в sys.argv это сам запускаемый сценарий, а дальше уже идут опции

    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:                   # o - название опции, a - ее значение
    if o == "-n":
        n = int(a)                  # запуск из командной строки :
    elif o == "-f":                 # (env) c:\repository\python_training>python data\\test.json generator\group.py -n 10 -f
        f = a


def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_uppercase + string.ascii_lowercase + string.digits + ""*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную


def random_phone(prefix, maxlen):
    phone = "+" + string.digits
    return prefix + "".join([random.choice(phone) for i in range(random.randrange(maxlen))])


def random_email(prefix):
    before_at = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase+ string.digits) for x in range(8)) # + "" * 10
    after_at = "@" + ''.join(random.choice(string.ascii_letters) for x in range(5)) #+ "." + ''.join(random.choice(string.ascii_letters) for x in range(3))
    return prefix + before_at + after_at


def random_address(prefix):
    adress = string.ascii_uppercase + string.ascii_lowercase + string.digits + "," #+ "."
    return prefix + ''.join(random.choice(adress) for x in range(15))

testdata = [Contact(firstname_of_contact="", lastname_of_contact="")] + [
            Contact(firstname_of_contact=random_string("firstname", 10), lastname_of_contact=random_string("lastname", 10), homenumber=random_phone("homephone",8),
                    contact_email=random_email("email"),contactaddress=random_address("adress"))
            for i in range(n)]
            # mobilenumber =random_phone("mobilphone",8), worknumber=random_phone("workphone",8), contact_phone2 =random_phone("phone2",8),
            #  contact_email2= random_email("email2"), contact_email3 = random_email("email3"), contact_address2 = random_address("adress2"), contact_notes = random_string("firstname", 20))

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)  # получаем информацию о пути к текущему файлу "../data/contacts.json"

with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata))# default=lambda x: x.__dict__, indent=2)) # __dict__хранит все свойства которые мы присваиваем в поля с self
                                                                            # функция dumps превращает некоторую структуру данных в строку в формате json
