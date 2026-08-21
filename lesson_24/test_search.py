import logging

import pytest
import requests
from requests.auth import HTTPBasicAuth

from hillel_automation__2026.lesson_24.conftest import BASE_URL, LOGGER_NAME, PASSWORD, USERNAME

logger = logging.getLogger(LOGGER_NAME)

# Кількість машин у cars_db серверної частини
TOTAL_CARS = 25
# Поле, за яким сервер сортує, якщо sort_by не передали
DEFAULT_SORT_FIELD = "brand"
CAR_FIELDS = ("brand", "year", "engine_volume", "price")

# Набори даних для GET /cars: (sort_by, limit)
SEARCH_PARAMS = [
    ("price", 5),
    ("year", 10),
    ("engine_volume", 3),
    ("brand", 1),
    ("price", TOTAL_CARS),
    (None, 4),          # без sort_by -> сервер сортує за brand
    ("price", None),    # без limit -> сервер повертає всі машини
]


@pytest.mark.cars_api
class TestCarsSearch:

    @pytest.fixture(scope="class")
    @classmethod
    def auth_session(cls):
        """
        Setup: одна сесія на весь клас - логінимось через HTTPBasicAuth
        і прописуємо отриманий access_token у заголовки сесії.
        Teardown: закриваємо сесію.
        """
        logger.info("Setup: створюємо requests.Session і виконуємо POST /auth")
        session = requests.Session()

        response = session.post(
            url=f"{BASE_URL}/auth",
            auth=HTTPBasicAuth(username=USERNAME, password=PASSWORD),
        )
        logger.debug(f"POST /auth -> {response.status_code}, body: {response.text}")

        assert response.status_code == 200, (
            f"Аутентифікація не пройшла: {response.status_code}, {response.text}"
        )

        access_token = response.json()["access_token"]
        session.headers.update({"Authorization": "Bearer " + access_token})
        logger.info(f"Токен отримано, довжина: {len(access_token)}")

        yield session

        logger.info("Teardown: закриваємо сесію")
        session.close()

    @pytest.mark.parametrize("sort_by, limit", SEARCH_PARAMS, ids=[
        "sort_by=price&limit=5",
        "sort_by=year&limit=10",
        "sort_by=engine_volume&limit=3",
        "sort_by=brand&limit=1",
        "sort_by=price&limit=25",
        "without_sort_by&limit=4",
        "sort_by=price&without_limit",
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        logger.info(f"GET /cars з параметрами: {params}")
        response = auth_session.get(url=f"{BASE_URL}/cars", params=params)
        logger.debug(f"URL запиту: {response.url}")
        logger.debug(f"Статус: {response.status_code}, тіло: {response.text}")

        assert response.status_code == 200, (
            f"Очікували 200, отримали {response.status_code}: {response.text}"
        )

        cars = response.json()
        assert isinstance(cars, list), f"Очікували список, отримали {type(cars)}"

        expected_count = min(limit, TOTAL_CARS) if limit is not None else TOTAL_CARS
        logger.info(f"Отримано машин: {len(cars)}, очікувалось: {expected_count}")
        assert len(cars) == expected_count, (
            f"limit={limit}: очікували {expected_count} записів, отримали {len(cars)}"
        )

        for car in cars:
            for field in CAR_FIELDS:
                assert field in car, f"У записі {car} немає поля {field}"

        sort_field = sort_by if sort_by is not None else DEFAULT_SORT_FIELD
        actual_order = [car[sort_field] for car in cars]
        logger.info(f"Порядок за полем '{sort_field}': {actual_order}")
        assert actual_order == sorted(actual_order), (
            f"Результат не відсортований за '{sort_field}': {actual_order}"
        )

    def test_search_cars_without_token(self):
        """Негативна перевірка: /cars захищений jwt_required."""
        logger.info("GET /cars без токена - очікуємо 401")
        response = requests.get(url=f"{BASE_URL}/cars", params={"sort_by": "price", "limit": 5})
        logger.debug(f"Статус: {response.status_code}, тіло: {response.text}")

        assert response.status_code == 401, (
            f"Очікували 401 без токена, отримали {response.status_code}: {response.text}"
        )
