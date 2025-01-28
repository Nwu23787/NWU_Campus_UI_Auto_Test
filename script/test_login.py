import pytest

from base.base_page import BasePage
from config import BASE_URL, LOGIN_URL
from page.login_page import LoginPage
from utils import DriverUtils, is_el_exist_by_text, get_json_data
from selenium.webdriver import ActionChains


@pytest.fixture(scope="class")
def init_login():
    driver = DriverUtils.get_driver()
    driver.maximize_window()
    driver.get(LOGIN_URL)
    yield driver
    DriverUtils.quit_driver()


@pytest.fixture(scope="function")
def init_login_success():
    yield
    LoginPage().logout()

@pytest.fixture(scope="function")
def init_login_error():
    yield
    DriverUtils.get_driver().refresh()


class TestLogin:
    @pytest.mark.parametrize('account,password', get_json_data("login_success"))
    def test_login_success(self, account, password, init_login, init_login_success):
        LoginPage().login(account, password)
        assert init_login.find_element_by_css_selector(".author")

    @pytest.mark.parametrize('account,password,expectText', get_json_data("login_error"))
    def test_login_error(self, account, password, expectText, init_login,init_login_error):
        LoginPage().login(account, password)
        assert is_el_exist_by_text(init_login, expectText)
