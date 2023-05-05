from datetime import datetime

from humps import camelize
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class BaseORMSchema(BaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
