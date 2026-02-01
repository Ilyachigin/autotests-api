from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email, get_random_string


public_users_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password=get_random_string(),
    lastName=get_random_string(),
    firstName=get_random_string(),
    middleName=get_random_string()
)
create_user_response = public_users_client.create_user(create_user_request)
print(f"Пользователь создан: {create_user_response}")

# Инициализация клиентов
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)

# Загрузка файла
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="clients/files/test.png"
)
create_file_response = files_client.create_file(create_file_request)
print(f"Файл загружен: {create_file_response}")

# Создание курса
create_course_request = CreateCourseRequestDict(
    title=get_random_string(),
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Курс создан: {create_course_response}")

# Создание задания
create_exercise_request = CreateExerciseRequestDict(
    title=get_random_string(),
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description="Python API exercise",
    estimatedTime="2 weeks"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Задание создано: {create_exercise_response}")
