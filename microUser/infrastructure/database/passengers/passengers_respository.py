
import asyncpg
from domain.repositories.passengers import passengers_repository as schema
from decouple import config
from loguru import logger
from infrastructure.database.Postresql import PostgreSQLException

PASSENGER_TABLE = config("PASSENGER_TABLE")


class PassengersRepository(schema.PassengersRepository):
    def __init__(self, conn: asyncpg.Pool):
        self.conn = conn
    
    async def get_passenger_by_email(self, email: str):
        try:
            async with self.conn.acquire() as conn:
                query = f"SELECT email, hashed_password FROM passenger.{PASSENGER_TABLE} WHERE email = $1"
                return await conn.fetchrow(query, email)
        except ConnectionError as e:
            logger.error(f"Error while connecting to Postgre: {e}")
            raise ConnectionError(f"Error while connecting to Postgre:  {e}")
        except Exception as e:
            logger.error(f"Error while retrieving events from Postgre: {e}")
            raise PostgreSQLException(
                f"Error while retrieving events from Postgre: {e}"
            )


        
        