from base.base_page import BasePage
from selenium.webdriver.common.by import By


class PostQuestionPage(BasePage):
    def __init__(self):
        super().__init__()
        self.title_input = "input[placeholder='标题']"
        self.tag_input = "input[placeholder='添加标签']"
        self.score = "input[placeholder='悬赏积分']"
        self.edit = "body"
        self.submit_btn = "button"
        self.dialog_close_btn = ".el-dialog__header button"


    def add_question(self, title, tag, score, text):
        # 输入标题
        if title is not None:
            self.input_text(self.find_ele(self.title_input), title)
        # 选择标签
        if tag is not None:
            # 点击标签框
            self.find_ele(self.tag_input).click()
            # 选择标签
            self.find_ele([By.XPATH, f"//span[text()='{tag}']"]).click()
            # 关闭对话框
            self.find_ele(self.dialog_close_btn).click()
        # 输入积分
        if score is not None:
            self.input_text(self.find_ele(self.score), score)
        # 输入正文
        if text is not None:
            # 切换 frame
            self.switch_frame(0)
            # 输入内容
            self.input_text(self.find_ele(self.edit), text)
            # 切换回默认 iframe
            self.switch_frame(None)
        # 点击提交按钮
        self.find_ele(self.submit_btn).click()
