import allure
import pytest
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Клик по лого «Яндекс»")
    @allure.description("Проверка, что клик по лого «Яндекс» перенаправляет на новую вкладку «Дзен»")
    def test_click_logo_ya_redirect_dzen(self, browser):
        main_page = MainPage(browser)
        main_page.click_to_logo_ya()
        assert main_page.check_redirect_dzen()

    @allure.title("Клик по лого «Самокат»")
    @allure.description("Проверка, что клик по лого «Самокат» перенаправляет на главную страницу")
    def test_click_logo_scooter_follow_link_main(self, browser):
        main_page = MainPage(browser)
        main_page.click_to_order_button_header()
        main_page.click_to_logo_scooter()
        assert main_page.check_main_page()

    @pytest.mark.parametrize('num, result', [(0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                                             (1,
                                              "Пока что у нас так: один заказ — один самокат. Если хотите покататься "
                                              "с друзьями, можете просто сделать несколько заказов — один за другим."),
                                             (2,
                                              "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в "
                                              "течение дня. Отсчёт времени аренды начинается с момента, "
                                              "когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в "
                                              "20:30, суточная аренда закончится 9 мая в 20:30."),
                                             (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                                             (4,
                                              "Пока что нет! Но если что-то срочное — всегда можно позвонить в "
                                              "поддержку по красивому номеру 1010."),
                                             (5,
                                              "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
                                              "суток — даже если будете кататься без передышек и во сне. Зарядка не "
                                              "понадобится."),
                                             (6,
                                              "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки "
                                              "тоже не попросим. Все же свои."),
                                             (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                                             ])
    @allure.title("Проверка вопросов и ответов на главной")
    @allure.description("Проверка, что ответы соответствуют заявленным")
    def test_check_questions_and_answers(self, browser, num, result):
        main_page = MainPage(browser)
        main_page.click_to_cookie_button()
        main_page.scroll_to_questions()
        main_page.get_question(num)
        assert main_page.get_answer(num) == result
