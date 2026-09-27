# Lesson 31 — Jenkins CI

Локальний Jenkins у Docker, який після кожного коміту запускає UI-тести
реєстрації на https://qauto2.forstudy.space/ (Playwright + pytest + Allure)
і публікує результати. Тести — ті самі, що в ДЗ 30, скопійовані сюди, щоб
папка була самодостатньою.

Увесь Jenkins описаний кодом: образ, плагіни, користувач, інструмент Allure
і сама джоба. Після `docker compose up` нічого не треба налаштовувати руками.

## Структура

```
lesson_31/
├── Jenkinsfile            # пайплайн: Checkout → Install → Run tests → Publish
├── docker-compose.yaml    # запуск Jenkins
├── jenkins/
│   ├── Dockerfile         # Jenkins + Python + Chromium для Playwright + Allure CLI
│   ├── plugins.txt        # Pipeline, Git, JUnit, Allure, JCasC, Job DSL
│   └── casc.yaml          # Configuration as Code: адмін, Allure, джоба
│
│   # тести (з ДЗ 30)
├── conftest.py            # фікстури + скріншот у Allure при падінні
├── pytest.ini             # --alluredir, --html, маркери
├── requirements.txt
├── test_registration.py   # 14 тестів з feature / story / step
└── core/                  # config, тестові дані, Page Object
```

## Пайплайн

| Етап | Що робить |
|---|---|
| Checkout | забирає код з GitHub (`checkout scm`) |
| Install dependencies | створює venv і ставить `lesson_31/requirements.txt` |
| Run tests | `pytest --junitxml=junit.xml` у `lesson_31` |
| Publish results | JUnit-результати, Allure-звіт, `report.html` як артефакт |

Якщо тести падають, збірка стає **UNSTABLE**, але етап публікації однаково
виконується: звіт найпотрібніший саме тоді, коли щось зламалось.

## Тригер «після кожного коміту»

Jenkins працює локально, тому GitHub не може надіслати йому вебхук.
Натомість `pollSCM('* * * * *')` раз на хвилину перевіряє гілку `homework_31`.
Є новий коміт — стартує збірка з причиною *Started by an SCM change*.

## Запуск тестів локально, без Jenkins

```bash
cd lesson_31
pip install -r requirements.txt && playwright install chromium
pytest ; allure serve allure-results
```

## Запуск Jenkins

```bash
cd lesson_31
docker compose up -d --build
```

Відкрити http://localhost:8080. Користувач `admin`, пароль за замовчуванням
`admin`. Змінити пароль: `JENKINS_ADMIN_PASSWORD=... docker compose up -d`.

Джоба `hillel-homework-31` створюється сама, перша збірка стартує протягом хвилини.

Зупинити:

```bash
docker compose down        # зберегти історію збірок
docker compose down -v     # видалити все разом з історією
```

## Нотатки

- Порт відкритий лише для `127.0.0.1`, з мережі Jenkins не видно.
- Chromium уже в образі (`/ms-playwright`), тому в збірці він не завантажується.
  Версія `playwright` в образі має збігатися з `requirements.txt`.
- `shm_size: 1gb` у compose: з дефолтними 64 MB Chromium у контейнері падає.
