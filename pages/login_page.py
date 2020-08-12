from .base_page import BasePage
from .locators import LoginPageLocators
import re

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        result = re.findall(r"/login/", self.url)
        assert len(result) == 1, f"Отсутствует подстрока login в данной ссылке. Полученные данные из подстроки = {result}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Отсутствует форма регистрации"
