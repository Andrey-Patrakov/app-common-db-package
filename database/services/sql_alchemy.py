from pydantic import BaseModel
from ..repositories import SQLAlchemyRepository
from ..utils import UnitOfWork


class SQLAlchemyService:
    repository: SQLAlchemyRepository

    async def create(self, model: BaseModel):
        model = model.model_dump()
        async with UnitOfWork() as uow:
            repository: SQLAlchemyRepository = self.repository(uow.session)
            result = await repository.create(**model)

        return result

    async def read(self, **filter_by):
        async with UnitOfWork() as uow:
            repository: SQLAlchemyRepository = self.repository(uow.session)
            result = await repository.read(**filter_by)

        return result

    async def read_one(self, **filter_by):
        async with UnitOfWork() as uow:
            repository: SQLAlchemyRepository = self.repository(uow.session)
            result = await repository.read_one(**filter_by)

        return result

    async def update(self, filter_by, **values):
        async with UnitOfWork() as uow:
            repository: SQLAlchemyRepository = self.repository(uow.session)
            result = await repository.update(filter_by=filter_by, **values)

        return result

    async def delete(self, delete_all: bool = False, **filter_by):
        async with UnitOfWork() as uow:
            repository: SQLAlchemyRepository = self.repository(uow.session)
            result = await repository.delete(
                delete_all=delete_all, **filter_by)

        return result
