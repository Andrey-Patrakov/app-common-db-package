from pydantic import BaseModel
from ..repositories import SQLAlchemyRepository


class SQLAlchemyService:

    def __init__(self, repository: SQLAlchemyRepository):
        self.repository: SQLAlchemyRepository = repository()

    async def create(self, model: BaseModel):
        model = model.model_dump()
        result = await self.repository.create(**model)
        return result

    async def read(self, **filter_by):
        return await self.repository.read(**filter_by)

    async def read_one(self, **filter_by):
        return await self.repository.read_one(**filter_by)

    async def update(self, filter_by, **values):
        return await self.repository.update(
            filter_by=filter_by, **values)

    async def delete(self, delete_all: bool = False, **filter_by):
        return await self.repository.delete(
            delete_all=delete_all, **filter_by)
