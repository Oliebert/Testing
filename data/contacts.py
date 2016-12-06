from model.contact import Contact
import random
import string                                                              # содержит константы хранящие списки символов

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
            for i in range(3)]