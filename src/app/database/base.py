from datetime import datetime

from humps import decamelize
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import func


@as_declarative()
class Base:
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return decamelize(cls.__name__)
