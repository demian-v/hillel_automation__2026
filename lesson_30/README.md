# Lesson 30 — PageObjectation (Allure)

ДЗ 26-28 (тести реєстрації на https://qauto2.forstudy.space/ з Page Object і фікстурами),
доповнене звітністю **Allure**.

> Базою взято ДЗ 26-28, бо саме там Page Object — і викладач попереджав, що ця
> домашка знадобиться для ДЗ 30-31.

## Що додано порівняно з ДЗ 26-28

| Вимога завдання | Як зроблено |
|---|---|
| Додати Allure | `allure-pytest` + `--alluredir=allure-results` у `pytest.ini` |
| Тести мають декоратор `feature` | `@allure.feature("Реєстрація користувача")` на всіх 14 тестах |
| Тести складаються зі step-ів | `@allure.step` на методах Page Object + `with allure.step(...)` у тестах |

Додатково:

- `@allure.epic` / `@allure.story` / `@allure.title` / `@allure.description` / `@allure.severity`
- скріншот і URL **автоматично чіпляються до звіту** при падінні тесту (`allure.attach`)
- дані згенерованого користувача додаються вкладенням — видно, на якому email упав тест
- блок ENVIRONMENT у звіті (base URL, браузер, headless, Python, платформа)
- паралельно генерується звіт `pytest-html` (`report.html`)

## Структура

```
lesson_30/
├── conftest.py                     # фікстури + allure.attach при падінні + environment
├── pytest.ini                      # --alluredir, --html, маркери
├── requirements.txt
├── test_registration.py            # 14 тестів з feature / story / step
└── core/
    ├── config.py
    ├── data/registration_data.py
    └── pages/                      # @allure.step на кожній дії зі сторінкою
        ├── base_page.py
        ├── main_page.py
        ├── signup_modal.py
        └── garage_page.py
```

## Запуск

```bash
pip install -r requirements.txt
playwright install chromium

pytest                      # тести + збір результатів у allure-results/
allure serve allure-results # відкрити звіт у браузері
```

Або згенерувати статичний звіт:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Інші варіанти запуску:

```bash
pytest --headed             # з видимим браузером
pytest -m positive          # тільки позитивні
pytest -m negative          # тільки негативні
```

> Потрібен Allure CLI: `brew install allure` (macOS) і встановлена Java.

## Групування у звіті

```
UI  (epic)
└── Реєстрація користувача  (feature)
    ├── Відкриття форми              2
    ├── Успішна реєстрація           1
    ├── Email дуплікат               1
    ├── Валідація обов'язкових полів 5
    └── Валідація значень полів      5
```

## Кроки

Кроки беруться з двох джерел і вкладаються один в одного:

- **Page Object** — кожна дія зі сторінкою (`Відкрити головну сторінку`,
  `Заповнити поле 'email' значенням '...'`, `Натиснути 'Register'`)
- **Тест** — блоки перевірок (`Кнопка 'Register' стала активною`,
  `Показано повідомлення 'Registration complete'`)

Приклад із звіту для `test_successful_registration`:

```
Заповнити форму реєстрації            5 sub-steps
Кнопка 'Register' стала активною
Натиснути 'Register' (очікуємо успіх)
Перевірити, що відкрилась сторінка 'Garage'
Показано повідомлення 'Registration complete'
```

Тестів без кроків немає — перевірено.

## Артефакти

`allure-results/`, `allure-report/` і `report.html` додані в `.gitignore` —
це згенеровані файли, вони відтворюються командами вище.

Результат: **14 passed**.
