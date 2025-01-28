from selenium.webdriver import ActionChains

from base.base_page import BasePage
from selenium.webdriver.common.by import By

from config import LOGIN_URL
from utils import DriverUtils


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 注册按钮
        self.register_btn = ".clearfix li:first-child .a-button"
        # 登录账号输入框
        self.account_input = "input[placeholder='账号']"
        # 登录密码输入框
        self.password_input = "input[placeholder='密码']"
        # 登录按钮
        self.login_btn = ".login-container button"
        # 右上角用户信息
        self.userinfo = ".author"
    def login(self, account, password):
        # 点击登录按钮
        if account is not None:
            # 输入账号
            self.input_text(self.find_ele(self.account_input), account)
        if password is not None:
            # 输入密码
            self.input_text(self.find_ele(self.password_input), password)
        # 点击登录
        self.find_ele(self.login_btn).click()

    def logout(self):
        # 若当前在登录状态，则退出登录
        try:
            ele = self.find_ele(self.userinfo)
            driver = DriverUtils.get_driver()
            # # 退出登录
            # action = ActionChains(driver)
            # action.move_to_element(ele).perform()
            # # 寻找退出登录按钮
            # self.find_ele(self.logout_btn).click()
            driver.execute_script('window.localStorage.clear()')
            # 刷新页面
            driver.get(LOGIN_URL)
        except Exception as e:
            # 处于非登录状态，不操作
            print(e)
            raise e