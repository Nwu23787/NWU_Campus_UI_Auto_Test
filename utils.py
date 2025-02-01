import json
import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_PATH


class DriverUtils:
    # 网站驱动对象
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


# 获取任意元素文本
def get_el_text(driver,css_selector):
    try:
        msg = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_css_selector(css_selector))
    except Exception as e:
        logging.error(f"没有获取到{css_selector}元素对应的文本！")
        msg = None
    return  msg

# 根据文本判断当前页面是否存在对应的元素对象
def is_el_exist_by_text(driver,text):
    try:
        flag = WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath(f"//*[text()='{text}']"))
    except Exception as e:
        flag = False
        # 截图
        DriverUtils.get_driver().get_screenshot_as_file(f"文本‘{text}’未找到对应元素.png")
        logging.error(f"未找到文本‘{text}’对应的元素")
    return flag

# 读取 JSON 文件数据
def get_json_data(file_name):
    file_path =BASE_PATH + f"/data/{file_name}.json"
    res = []
    with open(file=file_path,encoding="utf8") as f:
        all_data = json.load(f)

    for i in all_data.values():
        res.append(list(i.values()))
    return res