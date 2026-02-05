import uuid

from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class BasicUserModel(BaseModel):
    """
        Basic User Model Configuration
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


class UserSchema(BasicUserModel):
    """
        User Schema Fields
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BasicUserModel):
    """
        User Create Request Schema Fields
    """
    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BasicUserModel):
    """
        User Create Response Schema Fields
    """
    user: UserSchema

