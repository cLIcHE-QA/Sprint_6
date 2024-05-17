import allure

from pages.order_page import OrderPage

from data import Data

data = Data()


class TestOrderPage:

    @allure.title("Успешный заказ через кнопку «Заказать» в заголовке")
    @allure.description("Проверка успешного заказа самоката через кнопку «Заказать» в заголовке")
    def test_create_order_order_button_header_success(self, browser):
        order_page = OrderPage(browser)
        order_page.click_to_order_button_header()
        order_page.click_to_cookie_button()
        order_page.create_order(data.NAME, data.LASTNAME, data.ADDRESS, data.PHONE, data.DATE, data.COMMENT)
        assert order_page.check_order_page()

    @allure.title("Успешный заказ через кнопку «Заказать» внизу страницы")
    @allure.description("Проверка успешного заказа самоката через кнопку «Заказать» внизу главной страницы")
    def test_create_order_order_button_down_success(self, browser):
        order_page = OrderPage(browser)
        order_page.click_to_cookie_button()
        order_page.scroll_to_order_button_down()
        order_page.click_to_order_button_down()
        order_page.create_order(data.NAME, data.LASTNAME, data.ADDRESS, data.PHONE, data.DATE, data.COMMENT)
        assert order_page.check_order_page()
