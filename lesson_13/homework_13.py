'''Всім привіт
По домашці по логеру
В логері замініть basicConfig що там є на отакий:
  logging.basicConfig(
    filename='login_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s - %(levelname)s',
    force=True
    )

force=True обов'язково щоб все працювало
%(levelname)s якщо захочете додатково перевірити що правильний рівень логів приходить
в тестах використовуємо конструкцію with на читання файлу (див. лекцію №11)
Корисні функції:
file.read() - дозволить отримати контент файлу
content.splitlines() - дозволить розбити файл порядково і записати в список'''

"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s - %(levelname)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)