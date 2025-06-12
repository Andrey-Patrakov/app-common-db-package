from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, **values):
        raise NotImplementedError

    @abstractmethod
    async def read(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def update(self, filter_by, **values):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, delete_all: bool = False, **filter_by):
        raise NotImplementedError
