import random
import string
from dataclasses import dataclass

VALID_PASSWORD = "Password123"
ANOTHER_VALID_PASSWORD = "Password456"


@dataclass
class NewUser:
    name: str
    last_name: str
    email: str
    password: str
    repeat_password: str = None

    def __post_init__(self):
        if self.repeat_password is None:
            self.repeat_password = self.password


@dataclass
class InvalidFieldData:
    """Один невалідний сценарій: яке поле, яке значення, яку помилку очікуємо.

    expected_error — список рядків, бо одне повідомлення може мати кілька <p>.
    """
    field_name: str
    value: str
    expected_error: list[str]


def _random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def generate_new_user() -> NewUser:
    """Унікальний користувач — щоб тести не залежали один від одного."""
    return NewUser(
        name="Demian",
        last_name="Tester",
        email=f"aqa_{_random_string()}_{random.randint(1000, 9999)}@test.com",
        password=VALID_PASSWORD,
    )


PASSWORD_RULE_ERROR = (
    "Password has to be from 8 to 15 characters long and contain at least "
    "one integer, one capital, and one small letter"
)

EMPTY_FIELD_DATA = [
    InvalidFieldData("name", "", ["Name required"]),
    InvalidFieldData("last_name", "", ["Last name required"]),
    InvalidFieldData("email", "", ["Email required"]),
    InvalidFieldData("password", "", ["Password required"]),
    InvalidFieldData("repeat_password", "", ["Re-enter password required"]),
]

INVALID_FIELD_DATA = [
    InvalidFieldData(
        "name", "1",
        ["Name is invalid", "Name has to be from 2 to 20 characters long"],
    ),
    InvalidFieldData(
        "last_name", "2",
        ["Last name is invalid", "Last name has to be from 2 to 20 characters long"],
    ),
    InvalidFieldData("email", "bad-email", ["Email is incorrect"]),
    InvalidFieldData("password", "abc", [PASSWORD_RULE_ERROR]),
]
