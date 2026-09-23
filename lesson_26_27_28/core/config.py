import os

BASE_URL = os.getenv("QAUTO_BASE_URL", "https://qauto2.forstudy.space/")

# Basic-auth credentials for the study stand (given in the assignment)
BASIC_AUTH_USER = os.getenv("QAUTO_USER", "guest")
BASIC_AUTH_PASSWORD = os.getenv("QAUTO_PASSWORD", "welcome2qauto")

GARAGE_URL = f"{BASE_URL.rstrip('/')}/panel/garage"
