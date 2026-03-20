from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from clients.errors_schema import ValidationErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_create_file_with_empty_filename_response, \
    assert_create_file_with_empty_directory_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.suite(AllureFeature.FILES)
class TestFiles:

    @allure.title("Create file")
    @allure.severity(Severity.BLOCKER)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create file with empty filename")
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create file with empty directory")
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file="./testdata/files/image.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get file with incorrect file id")
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, function_file: FileFixture):
        file_id = "incorrect-file-id"

        response = files_client.get_file_api(file_id)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

