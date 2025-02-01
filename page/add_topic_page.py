from time import sleep

from base.base_page import BasePage
from selenium.webdriver.common.by import By

from utils import DriverUtils


class AddTopicPage(BasePage):
    def __init__(self):
        super().__init__()
        self.select_arrow = ".el-input__suffix"
        self.title_input = "input[placeholder='标题']"
        self.edit = "body"
        self.submit_btn = ".asterisk-left button"

    def add_topic(self, tag, title, text):
        if tag is not None:
            # 点击下拉框
            self.find_ele(self.select_arrow).click()
            # 选择标签
            self.find_ele((By.XPATH, f"//span[text()='{tag}']")).click()
        if title is not None:
            # 输入标题
            self.input_text(self.find_ele(self.title_input), title)
        if text is not None:
            # 切换 frame
            self.switch_frame(0)
            # 输入内容
            self.input_text(self.find_ele(self.edit), text)
            # 切换回默认 iframe
            self.switch_frame(None)
        # 提交
        self.find_ele(self.submit_btn).click()

