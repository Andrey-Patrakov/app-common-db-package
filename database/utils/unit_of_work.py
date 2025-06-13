from .session import async_session_maker


class UnitOfWork:

    async def __aenter__(self):
        self.session = async_session_maker()
        return self

    async def __aexit__(self, exception_type, exception_value, traceback):
        try:
            if exception_value:
                raise exception_value

            await self.commit()

        except Exception as e:
            await self.rollback()
            raise e

        finally:
            await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
