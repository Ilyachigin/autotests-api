from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import get_random_email, get_random_string


public_users_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password=get_random_string(),
    last_name=get_random_string(),
    first_name=get_random_string(),
    middle_name=get_random_string()
)
create_user_response = public_users_client.create_user(create_user_request)
print(f"Пользователь создан: {create_user_response}")

# Инициализация клиентов
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Загрузка файла
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="clients/files/test.png"
)
create_file_response = files_client.create_file(create_file_request)
print(f"Файл загружен: {create_file_response}")

# Создание курса
create_course_request = CreateCourseRequestSchema(
    title=get_random_string(),
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Курс создан: {create_course_response}")

# Создание задания
create_exercise_request = CreateExerciseRequestSchema(
    title=get_random_string(),
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=1,
    description="Python API exercise",
    estimated_time="2 weeks"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Задание создано: {create_exercise_response}")
