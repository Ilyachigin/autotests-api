import time


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


def get_random_string() -> str:
    return str(int(time.time() * 1000))

