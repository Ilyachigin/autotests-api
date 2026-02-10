from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import get_random_email, get_random_string


public_users_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password=get_random_string(),
    lastName=get_random_string(),
    firstName=get_random_string(),
    middleName=get_random_string()
)
create_user_response = public_users_client.create_user(create_user_request)
print(f"Пользователь создан: {create_user_response}")

# Инициализация юзера
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

# Получение данных юзера
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Валидация схемы получения данных юзера
validate(
    schema=get_user_response.json(),
    instance=get_user_response_schema,
    format_checker=Draft202012Validator.FORMAT_CHECKER,
)
