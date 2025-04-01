from abc import ABC, abstractmethod


class PassengersRepository(ABC):
    @abstractmethod
    async def get_passenger_by_email(self, email: str):
        """Authenticates passenger against our passengers.users table"""
        raise NotImplementedError