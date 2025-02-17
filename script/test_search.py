from time import sleep

import pytest

from config import INDEX_URL
from page.index_page import IndexPage
from utils import is_el_exist_by_text, DriverUtils, get_json_data


@pytest.fixture(scope="function")
def init_search():
    # 跳转到首页
    driver = DriverUtils.get_driver()
    driver.get(INDEX_URL)
    yield driver
    DriverUtils.quit_driver()


class TestSearch:
    @pytest.mark.parametrize('keywords, result_keywords', get_json_data("search_success"))
    def test_search_success(self, keywords, result_keywords, init_search):
        IndexPage().search(keywords)
        assert is_el_exist_by_text(init_search, result_keywords, False)

    def test_search_null(self, init_search):
        IndexPage().search("")
        assert init_search.find_element_by_css_selector(".postTopicButton")

    def test_search_no_result(self, init_search):
        IndexPage().search("noresult")
        assert is_el_exist_by_text(init_search, "没有找到相关记录", True)
