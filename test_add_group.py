
from group import Group
from application import Application

import time, unittest
import pytest




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_test_add_group(app):


    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.group_creation( Group(name="knlnölnlmlml", header="GUBJHB", footer="lknlknkln"))
    app.return_to_group()
    app.logout()


def test__add_empty_group(app):


    app.open_home_page()
    app.login( username="admin", password="secret")
    app.open_groups_page()
    app.group_creation( Group(name="", header="", footer=""))
    app.return_to_group()
    app.logout()





