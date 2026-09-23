# Lesson 26–27–28 — Playwright + Page Object

Тест процесу реєстрації користувача на https://qauto2.forstudy.space/

## Що зроблено

- **Page Object** для кожної частини застосунку: головна сторінка, модальне вікно
  реєстрації, сторінка гаража.
- **Фікстури** для підготовки стану: basic-auth на рівні контексту, відкрита головна
  сторінка, відкрите модальне вікно, унікальні дані користувача, вже зареєстрований
  користувач.
- **Авто-скріншот** при падінні тесту (`screenshots/<test_name>.png`).

## Структура

```
lesson_26_27_28/
├── conftest.py                     # фікстури + хук зі скріншотами
├── pytest.ini                      # маркери та параметри запуску
├── test_registration.py            # тести реєстрації
└── core/
    ├── config.py                   # base url + basic-auth креденшели
    ├── data/registration_data.py   # дата-класи, генератор користувача, набори помилок
    └── pages/
        ├── base_page.py            # спільна основа + toast-повідомлення
        ├── main_page.py            # головна сторінка (кнопка Sign up)
        ├── signup_modal.py         # форма "Registration"
        └── garage_page.py          # сторінка після успішної реєстрації
```

## Запуск

```bash
pip install -r requirements.txt
playwright install chromium

pytest                    # headless
pytest --headed           # з видимим браузером
pytest -m positive        # тільки позитивні сценарії
pytest -m negative        # тільки негативні сценарії
```

Базовий URL і креденшели за потреби перевизначаються через змінні оточення
`QAUTO_BASE_URL`, `QAUTO_USER`, `QAUTO_PASSWORD`.

## Покриті сценарії

| Тест | Перевірка |
|---|---|
| `test_signup_modal_is_opened` | кнопка Sign up відкриває форму, Register неактивна |
| `test_successful_registration` | валідні дані → гараж + "Registration complete" |
| `test_registration_with_existing_email` | дубль email → "User already exists", форма лишається відкритою |
| `test_empty_required_field` (×5) | порожнє обов'язкове поле → "... required" |
| `test_invalid_field_value` (×4) | невалідне значення → правило валідації поля |
| `test_passwords_do_not_match` | різні паролі → "Passwords do not match" |
| `test_register_button_stays_disabled_until_form_is_valid` | Register вмикається лише на повній формі |

Результат: **14 passed**.
