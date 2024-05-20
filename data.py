import random


class Data:
    NAMES = ["Артем", "Ангелина", "Света", "Владимир", "Роман", "Андрей"]
    NAME = random.choice(NAMES)

    LASTNAMES = ["Стопов", "Разумовская", "Бушев", "Медведева", "Крылатов", "Соболев"]
    LASTNAME = random.choice(LASTNAMES)

    ADDRESSES = ["Санкт-Петербург, Невский проспект, 85", "Москва, Перовская улица 10",
                 "Муром, Комсомольская улица, 51"]
    ADDRESS = random.choice(ADDRESSES)

    PHONE = f'+7{random.randint(9000000000, 9999999999)}'

    DATES = ["01.05.2024", "31.05.2024"]
    DATE = random.choice(DATES)

    COMMENTS = ["Без комментариев", "Позвонить заранее"]
    COMMENT = random.choice(COMMENTS)
