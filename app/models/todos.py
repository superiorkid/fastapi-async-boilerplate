import datetime

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.models.mixins import Mixins


class Todo(Base, Mixins):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    deleted_at: Mapped[datetime.datetime | None]

    def __repr__(self) -> str:
        return f"Todo(id={self.id})"
