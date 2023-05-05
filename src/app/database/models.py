# Import all the models, so that Base has them before being
# imported by Alembic
from app.blog import models  # noqa
from app.database.base import Base  # noqa
