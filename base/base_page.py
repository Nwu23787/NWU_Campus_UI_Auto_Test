import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utils import DriverUtils


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()

    # 公用元素定位方法
    # 调用该定位时，使用显示等待的方式定位元素
    # 记录代码执行定位的日志
    def find_ele(self, location):
        try:
            # 个人习惯，默认使用CSS查找元素
            if not isinstance(location, (tuple, list)):
                location = [location]
            if len(location) == 1:
                location = (By.CSS_SELECTOR, location[0])
            ele = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*location))
        except Exception as e:
            ele = None
            logging.error(f"未找到{location}元素")

        return ele

    # 输入框输入文本
    def input_text(self, ele, text):
        try:
            ele.clear()
            ele.send_keys(text)
            logging.info(f"input {text} success.")
        except Exception as e:
            logging.error(f"input ‘{text}’ failed.")

    # 切换窗口
    def switch_window(self, n):
        try:
            # 获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[n])
            # 打印日志
            logging.info(f"switch to {n} window success.")

        except Exception as e:
            logging.error(f"switch to {n} window failed!")

    # frame切换
    def switch_frame(self, ele):
        # 切换指定iframe标签
        try:
            if ele is None:
                self.driver.switch_to_default_content()
            else:
                self.driver.switch_to.frame(ele)
                logging.info(f"switch to {ele} iframe success.")
        except Exception as e:
            # 打印日志
            logging.info(f"switch to {ele} iframe failed!")
