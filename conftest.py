import pytest
from fixture.application import Application


fixture=None #фикстура не определена

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser") # получаем доступ к сохраненному параметру browser
    base_url = request.config.getoption("--baseUrl")

    if fixture is None:    #случай если фикстура не определена

        fixture = Application(browser = browser, base_url= base_url)

    else:                           #случай если фикстура испортилась
        if not fixture.is_valid():

            fixture = Application(browser = browser, base_url= base_url) # browser = browser, base_url=base_url

    fixture.session.ensure_login(username="admin", password="secret")

    return fixture

@pytest.fixture(scope="session", autouse=True) # фикстура выполняется автоматически
def stop(request):

    def fin():

        fixture.session.ensure_logout() #убеждаемся что мы вывшли из системы
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption ("--browser", action= "store", default="firefox" ) # действие - сохранить значение параметра browser
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")