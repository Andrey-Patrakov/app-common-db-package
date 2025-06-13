from sqlalchemy import text
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError, ProgrammingError


async def create_database_if_not_exists(url):
    url = make_url(url)
    db_name = url.database
    engine = None

    db_exists = False
    try:
        engine = create_async_engine(url, isolation_level='AUTOCOMMIT')
        query = text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        async with engine.connect() as connection:
            db_exists = bool(await connection.scalar(query))

    except (ProgrammingError, OperationalError):
        pass

    finally:
        if engine:
            await engine.dispose()

    if not db_exists:
        url = url._replace(database='postgres')
        engine = create_async_engine(url, isolation_level='AUTOCOMMIT')
        query = text(f''' CREATE DATABASE "{db_name}" ENCODING 'utf8' ''')
        async with engine.connect() as connection:
            await connection.execute(query)

        await engine.dispose()
