import pytest

from config import POST_QUESTION_URL, LOGIN_URL
from page.login_page import LoginPage
from page.post_question_page import PostQuestionPage
from utils import is_el_exist_by_text, DriverUtils, get_json_data


@pytest.fixture(scope="class")
def init_post_question():
    driver = DriverUtils.get_driver()
    # driver.get(POST_QUESTION_URL)
    driver.get(LOGIN_URL)
    LoginPage().login("hello", "12345678")
    yield driver
    DriverUtils.quit_driver()


@pytest.fixture
def refresh_page():
    driver = DriverUtils.get_driver()
    driver.get(POST_QUESTION_URL)
    return


class TestAddQuestion:
    @pytest.mark.parametrize('title, tag, score, text, expectText', get_json_data("post_question"))
    def test_add_question_success(self, title, tag, score, text, expectText, init_post_question, refresh_page):
        PostQuestionPage().add_question(title, tag, score, text)
        assert is_el_exist_by_text(init_post_question, expectText, True)
