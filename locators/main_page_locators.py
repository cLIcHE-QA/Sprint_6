from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_HEADER = [By.XPATH, ".//div[contains(@class, 'Home_Header')]"]  # Заголовок на главной странице
    QUESTION_ITEM = [By.ID, "accordion__heading-{}"]  # Вопросы
    ANSWER_ITEM = [By.ID, "accordion__panel-{}"]  # Ответы
    IMPORTANT_QUESTION = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # Блок «Вопросы о важном»
    ORDER_BUTTON_DOWN = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]  #
    # Кнопка «Заказать» внизу страницы
