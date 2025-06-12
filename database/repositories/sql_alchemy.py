from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import SQLAlchemyError

from .base import AbstractRepository
from ..utils import async_session_maker


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create(self, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    insert(self.model)
                    .values(**values)
                    .returning(self.model))
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

                return result

    async def read(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    async def read_one(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def update(self, filter_by, **values):
        async with async_session_maker() as session:
            async with session.begin():
                where = [
                    getattr(self.model, k) == v for k, v in filter_by.items()]

                query = (
                    update(self.model)
                    .where(*where)
                    .values(**values)
                    .execution_options(synchronize_session='fetch'))
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

                return result.rowcount

    async def delete(self, delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError(
                'You must specify at least one parameter.')

        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    delete(self.model)
                    .filter_by(**filter_by))
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

                return result.rowcount
