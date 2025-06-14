from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .base import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **values):
        query = (
            insert(self.model)
            .values(**values)
            .returning(self.model))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def read(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def read_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def update(self, filter_by, **values):
        where = [getattr(self.model, k) == v for k, v in filter_by.items()]
        query = (
            update(self.model)
            .where(*where)
            .values(**values)
            .execution_options(synchronize_session='fetch'))
        result = await self.session.execute(query)
        return result.rowcount

    async def delete(self, delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError('You must specify at least one parameter.')

        query = (delete(self.model).filter_by(**filter_by))
        result = await self.session.execute(query)
        return result.rowcount
