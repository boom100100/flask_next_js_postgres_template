from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from app.app import db


class Example(db.Model):
    __tablename__ = "examples"

    id: Mapped[int] = mapped_column(primary_key=True)
