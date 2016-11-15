import pytest
from fixture.application import Application


fixture=None #фикстура не определена

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:             #случай если фикстура не определена

        fixture = Application()

    else:                           #случай если фикстура испортилась
        if not fixture.is_valid():
            fixture = Application()

    fixture.session.ensure_login(username="admin", password="secret")

    return fixture

@pytest.fixture(scope="session", autouse=True) # фикстура выполняется автоматически
def stop(request):

    def fin():

        fixture.session.ensure_logout() #убеждаемся что мы вывшли из системы
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
