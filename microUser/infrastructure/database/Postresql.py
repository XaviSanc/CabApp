from decouple import config
import asyncpg
from loguru import logger

POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_DB = config("POSTGRES_DB")
POSTGRES_HOST = config("POSTGRES_HOST")
POSTGRES_PORT = config("POSTGRES_PORT")
POSTGRES_URL = config("POSTGRES_URL")

class PostgreSQLException(Exception):
    pass

class PostgreSQL:
    conn: asyncpg.Pool | None = None

    @staticmethod
    async def connect():
        
        if PostgreSQL.conn is None:

            PostgreSQL.conn = await asyncpg.create_pool(
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                database=POSTGRES_DB,
                host=POSTGRES_HOST,
                port=POSTGRES_PORT,
                    max_inactive_connection_lifetime=5,
                    max_size=10 #default
            )

    @staticmethod
    async def close():
        if PostgreSQL.conn:
            await PostgreSQL.conn.close()
            PostgreSQL.conn = None

    @staticmethod
    async def fetch(query: str, *args):
        async with PostgreSQL.conn.acquire() as connection:
            return await connection.fetch(query, *args)

    @staticmethod
    async def execute(query: str, *args):
        async with PostgreSQL.conn.acquire() as connection:
            return await connection.execute(query, *args)
        

async def get_db():
    postgresql = None
    if PostgreSQL.conn is None:
        logger.warning("PostgreSQL is not connected. Attempting to reconnect...")
        try:
            postgresql = PostgreSQL()
            await postgresql.connect()
        except ConnectionError as e:
            logger.error(f"Connection error with PostgreSQL: {e}")
            raise PostgreSQLException(f"Connection error with PostgreSQL: {e}")
    return postgresql.conn if postgresql is not None else PostgreSQL.conn


async def initialize_database():

    try:
        conn = PostgreSQL().conn
        await conn.execute("CREATE SCHEMA IF NOT EXISTS driver;")
        await conn.execute("CREATE SCHEMA IF NOT EXISTS passenger;")
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS driver.test (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                license_number TEXT UNIQUE NOT NULL
            );
        """)

        await conn.execute("""
            CREATE TABLE IF NOT EXISTS passenger.test (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)

        await conn.execute("INSERT INTO driver.test (name, license_number) VALUES ('John Doe', 'DR12345') ON CONFLICT DO NOTHING;")
        await conn.execute("INSERT INTO passenger.test (name, email) VALUES ('Jane Smith', 'jane@example.com') ON CONFLICT DO NOTHING;")

    except ConnectionError as e:
        raise e from e
    except Exception as e:
        logger.error(f"Unknown exception from Mongo: {e}")
        raise PostgreSQLException(f"Unknown exception from PostregSQL {e}")
