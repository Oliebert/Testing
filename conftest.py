import pytest
from fixture.application import Application
import json
import os.path
import importlib


fixture = None                                                                                   #фикстура не определена
target = None


@pytest.fixture
def app(request):

    global fixture
    global target
    browser = request.config.getoption("--browser")                   # получаем доступ к сохраненному параметру browser

    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # получаем информацию о пути к текущему файлу
        with open(config_file) as f:                                                                        # затем пришиваем к ней target
            target = json.load(f)

    if fixture is None or not fixture.is_valid():                                   # случай если фикстура не определена
        fixture = Application(browser=browser, base_url=target['baseUrl'])                              # или не валидна
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)                                      # фикстура выполняется автоматически
def stop(request):

    def fin():

        fixture.session.ensure_logout()                                            # убеждаемся что мы вывшли из системы
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):

    parser.addoption("--browser", action="store", default="firefox")  # действие - сохранить значение параметра browser
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc): # параметр metafunc содержит информацию о вызываемом методе, для которого генерируются данные
                                     #в частности, он содержит информацию о фикстурах, которые требуются этому методу
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:]) # загружаем тестовые данные из модуля, который имеет такое же название как фикстура только обрезанное
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata # или ('.' + <имя модуля>, имя данных)