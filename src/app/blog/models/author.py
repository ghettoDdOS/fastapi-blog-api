import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Author(Base):
    first_name: Mapped[str] = mapped_column(
        sa.String(length=30),
    )
    last_name: Mapped[str] = mapped_column(
        sa.String(length=30),
    )
    email: Mapped[str] = mapped_column(
        sa.String(length=50),
        unique=True,
    )
    phone: Mapped[str] = mapped_column(
        sa.String(length=15),
        unique=True,
    )
