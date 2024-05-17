from selenium.webdriver.common.by import By


class BasePageLocators:
    YANDEX_LOGO = [By.XPATH, ".//img[@alt='Yandex']"]  # Логотип «Яндекс»
    SCOOTER_LOGO = [By.XPATH, ".//img[@alt='Scooter']"]  # «Логотип Самокат»
    ORDER_BUTTON = [By.XPATH,
                           ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"]  # Кнопка «Заказать» в
    # хедере
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]  # Кнопка принятия cookies
    DZEN_HEADER = [By.ID, "dzen-header"]  # Заголовок на странице «Дзен»
