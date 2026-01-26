import httpx
from httpx import Response


class UserClient:

    def __init__(self):
        self.http = httpx.Client(
            base_url="http://localhost:8000/api/v1",
            headers={"Content-Type": "application/json"}
        )

    def authentication(self) -> str:
        payload = {
            "email": "user@example.com",
            "password": "string"
        }

        response = self.http.post("/authentication/login", json=payload)
        response.raise_for_status()

        return response.json()["token"]["accessToken"]

    def get_user(self, bearer_token: str) -> Response:
        response = self.http.get(
            "/users/me",
            headers={"Authorization": f"Bearer {bearer_token}"}
        )
        response.raise_for_status()

        return response


if __name__ == '__main__':
    user = UserClient()
    token = user.authentication()
    profile = user.get_user(token)

    print(f"Status code: {profile.status_code}")
    print(f"User response: {profile.json()}")

