
from fastapi import HTTPException
from domain.entities.passengers.token import Token
from domain.repositories.passengers.passengers_repository import PassengersRepository
from domain.services.auth_service import AuthService, AuthServiceException, InvalidCredentials
from infrastructure.database.Postresql import PostgreSQLException


class LoginPassengerUseCaseError(HTTPException):
    def __init__(self, detail: str = "Login failed", status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)

class InvalidCredentialsException(LoginPassengerUseCaseError):
    def __init__(self):
        super().__init__(detail="Invalid credentials", status_code=401)

class DatabaseException(LoginPassengerUseCaseError):
    def __init__(self):
        super().__init__(detail="Database error", status_code=500)

class AuthServiceException(LoginPassengerUseCaseError):
    def __init__(self):
        super().__init__(detail="Authentication service error", status_code=500)

class LoginPassengerUseCase:

    def __init__(self, passengers_repository: PassengersRepository):
        self.passengers_repository = passengers_repository

    async def execute(self, email: str, password: str):
        try:
            user = await self.passengers_repository.get_passenger_by_email(email)
            if user is None or not AuthService.verify_password(password, user["hashed_password"]):
                raise InvalidCredentialsException()  # 401 instead of generic Exception
            
            access_token = AuthService.create_access_token(
                data={"email": user["email"], "role": "PASSENGER"}
            )
            return Token(access_token=access_token, token_type="bearer")
        
        except PostgreSQLException as e:
            raise DatabaseException()
        
        except InvalidCredentialsException as e:
            raise InvalidCredentialsException()
        
        except InvalidCredentials as e:
            raise InvalidCredentialsException()

        except AuthServiceException as e:
            raise AuthServiceException()

        except Exception as e:
            raise LoginPassengerUseCaseError(detail=f"Unexpected error: {str(e)}", status_code=500)


    