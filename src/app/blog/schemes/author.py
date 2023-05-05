from app.common.schemas import BaseORMSchema, BaseSchema


class BaseAuthor(BaseSchema):
    first_name: str
    last_name: str
    email: str
    phone: str


class AuthorRequest(BaseAuthor):
    pass


class AuthorResponse(BaseAuthor, BaseORMSchema):
    pass
