from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_TITLE_FIRST_STEP = [By.XPATH, ".//div[text()='Для кого самокат']"]  # Заголовок на первом шаге заказа самоката
    NAME_FIELD = [By.XPATH, ".//input[@placeholder='* Имя']"]  # Поле «Имя»
    LASTNAME_FIELD = [By.XPATH, ".//input[@placeholder='* Фамилия']"]  # Поле «Фамилия»
    ADDRESS_FIELD = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]  # Поле «Адрес»
    METRO_FIELD = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  # Поле «Станция метро»
    CHOOSE_METRO = [By.XPATH, ".//li[@data-value={num}]"]  # Список станций метро
    PHONE_FIELD = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле «Телефон»
    ONWARD_BUTTON = [By.XPATH, ".//button[text()='Далее']"]  # Кнопка «Далее»
    ORDER_TITLE_SECOND_STEP = [By.XPATH, ".//div[text()='Про аренду']"]  # Заголовок на втором шаге заказа самоката
    WHEN_FIELD = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  # Поле «Когда привезти самокат»
    CHOOSE_DATE = (By.XPATH, ".//div[contains(@class, 'selected')]")  # Выбранная дата в календаре
    LIMIT_FIELD = [By.XPATH, ".//div[text()='* Срок аренды']"]  # Поле «Срок аренды»
    CHOOSE_LIMIT = [By.CLASS_NAME, "Dropdown-option"]  # Список срока аренды
    CHOOSE_SCOOTER = [By.XPATH, ".//label[contains(@class, 'Checkbox_Label')]"]  # Выбор цвета самоката
    COMMENT_FIELD = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]  # Поле «Комментарий для курьера»
    ORDER_BUTTON_UNDER_FORM = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"]  #
    # Кнопка «Заказать» под формой ввода
    CONFIRMATION_WINDOW = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"]  # Заголовок в попапе
    # подтверждения заказа
    AGREE_BUTTON = [By.XPATH, ".//button[text()='Да']"]  # Кнопка «Да» в попапе подтверждении заказа
    STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]  # Кнопка «Посмотреть статус»
    CANCEL_BUTTON = [By.XPATH, ".//button[text()='Отменить заказ']"]  # Кнопка «Отменить заказ»
