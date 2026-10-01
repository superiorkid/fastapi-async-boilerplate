import datetime
import decimal
from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy import DateTime, MetaData, Numeric
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import get_settings

settings = get_settings()


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    type_annotation_map: dict[Any, Any] = {
        datetime.datetime: DateTime(timezone=True),
        decimal.Decimal: Numeric(precision=10, scale=2),
    }


engine = create_async_engine(
    settings.database_url.get_secret_value(),
    echo=settings.debug,
    pool_size=20,  # Keep 20 connections ready
    max_overflow=40,  # Allow 40 more during spikes
    pool_timeout=30,  # Wait 30s for connection
    pool_recycle=3600,  # Recycle every hour
    pool_pre_ping=True,  # Test connection before use
)
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
