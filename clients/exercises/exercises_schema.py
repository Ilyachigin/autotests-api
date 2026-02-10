from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class BaseExerciseModel(BaseModel):
    """
    Описание базовой модели задания.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


class ExerciseSchema(BaseExerciseModel):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str = Field()
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseExerciseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseExerciseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseExerciseModel):
    """
    Описание структуры запроса на получение задания.
    """
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(BaseExerciseModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseExerciseModel):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseExerciseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseExerciseModel):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: ExerciseSchema
