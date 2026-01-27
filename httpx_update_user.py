import httpx
from tools import fakers

from httpx import Response


class UserClient:

    def __init__(self):
        self.http = httpx.Client(
            base_url="http://localhost:8000/api/v1",
            headers={"Content-Type": "application/json"}
        )
        self.fake_email = fakers.get_random_email()
        self.fake_string = fakers.get_random_string()

    def create_user(self) -> str:
        payload = {
            "email": self.fake_email,
            "password": self.fake_string,
            "lastName": self.fake_string,
            "firstName": self.fake_string,
            "middleName": self.fake_string
        }

        response = self.http.post("/users", json=payload)
        response.raise_for_status()

        return response.json()["user"]["id"]

    def update_user(self, user_id: str, access_token: str) -> Response:
        payload = {
            "email": fakers.get_random_email(),
            "lastName": fakers.get_random_string(),
            "firstName": fakers.get_random_string(),
            "middleName": fakers.get_random_string()
        }

        response = self.http.patch(
            f"/users/{user_id}",
            headers={"Authorization": f"Bearer {access_token}"},
            json=payload
        )
        response.raise_for_status()

        return response.json()["user"]

    def authentication(self) -> str:
        payload = {
            "email": self.fake_email,
            "password": self.fake_string
        }

        response = self.http.post("/authentication/login", json=payload)
        response.raise_for_status()

        return response.json()["token"]["accessToken"]


if __name__ == '__main__':
    user = UserClient()

    created_user_id = user.create_user()
    print(f"User created: {created_user_id}")

    token = user.authentication()
    user_data = user.update_user(created_user_id, token)
    print(f"User updated data: {user_data}")

