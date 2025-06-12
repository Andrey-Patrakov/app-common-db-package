from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from ..config import db_settings


def get_pg_url():
    url = f'postgresql+asyncpg://{db_settings.USER}:{db_settings.PASSWORD}'
    url += f'@{db_settings.HOST}:{db_settings.PORT}/{db_settings.NAME}'
    return url


DATABASE_URL = get_pg_url()
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
