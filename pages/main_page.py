import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажать на лого «Яндекс»")
    def click_to_logo_ya(self):
        self.click_to_element(BasePageLocators.YANDEX_LOGO)

    @allure.step("Нажать на лого «Самокат»")
    def click_to_logo_scooter(self):
        self.click_to_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на кнопку «Заказать»")
    def click_to_order_button_header(self):
        self.click_to_element(BasePageLocators.ORDER_BUTTON)

    @allure.step("Проверить, что перешли на главную страницу")
    def check_main_page(self):
        return self.find_definite_element(MainPageLocators.MAIN_HEADER)

    @allure.step("Проверить, что открылась страница «Дзен»")
    def check_redirect_dzen(self):
        self.redirect_new_tab()
        return self.find_definite_element(BasePageLocators.DZEN_HEADER)

    @allure.step("Нажать на кнопку «Да все привыкли»")
    def click_to_cookie_button(self):
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step("Проскроллить до блока «Вопросы о важном»")
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.IMPORTANT_QUESTION)
        return self.find_definite_element(MainPageLocators.IMPORTANT_QUESTION)

    @allure.step("Нажать на вопрос")
    def get_question(self, num):
        method, locator = MainPageLocators.QUESTION_ITEM
        locator = locator.format(num)
        self.click_to_element((method, locator))
        return self.find_definite_element((method, locator))

    @allure.step("Сравнить тексты ответов")
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_ITEM
        locator = locator.format(num)
        return self.find_definite_element((method, locator)).text
