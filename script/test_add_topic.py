from time import sleep

import pytest

from config import TOPIC_URL, INDEX_URL, LOGIN_URL
from page.add_topic_page import AddTopicPage
from page.login_page import LoginPage
from utils import DriverUtils, is_el_exist_by_text, get_json_data


@pytest.fixture(scope="class")
def init_login():
    driver = DriverUtils().get_driver()
    driver.get(LOGIN_URL)
    LoginPage().login("hello", "12345678")
    driver.get(TOPIC_URL)
    yield driver


@pytest.fixture()
def refresh_page():
    DriverUtils.get_driver().get(TOPIC_URL)


class TestTopic:
    @pytest.mark.parametrize('tag, title, text', get_json_data("add_topic_success"))
    def test_add_topic_success(self, tag, title, text, init_login, refresh_page):
        AddTopicPage().add_topic(tag, title, text)
        # 检验 若跳转首页则表示成功
        assert is_el_exist_by_text(init_login, "提交成功，3秒后自动跳转到首页")

    @pytest.mark.parametrize('tag, title, text, expectText',get_json_data("add_topic_error"))
    def test_add_topic_error(self, tag, title, text, expectText, init_login, refresh_page):
        AddTopicPage().add_topic(tag, title, text)
        assert is_el_exist_by_text(init_login, expectText)
