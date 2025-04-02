
from typing import Annotated
import asyncpg
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from application.passengers.use_cases.passenger_login import LoginPassengerUseCase, LoginPassengerUseCaseError
from infrastructure.database.Postresql import PostgreSQLException, get_db
from domain.entities.passengers.token import Token
from infrastructure.database.passengers.passengers_respository import PassengersRepository
from domain.services.auth_service import AuthServiceException
from loguru import logger

router = APIRouter(prefix="/auth")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="api/auth/v1/passengers/login")  

def get_passenger_repository(conn: Annotated[asyncpg.Pool, Depends(get_db)]) -> PassengersRepository:
    return PassengersRepository(conn)

def get_login_use_case(repository: Annotated[PassengersRepository, Depends(get_passenger_repository)]) -> LoginPassengerUseCase:
    return LoginPassengerUseCase(repository)

@router.post("/v1/passengers/login", response_model=Token)
async def login_for_passenger(
    use_case: Annotated[LoginPassengerUseCase, Depends(get_login_use_case)],
    form_data: OAuth2PasswordRequestForm = Depends(),
    )->Token:
    try:
        return await use_case.execute(form_data.username, form_data.password)
    except HTTPException as e:  
        raise e 
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True) 
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again later.")

  
@router.get("/v1/test")
async def test(token = Depends(oauth2_schema)):
    raise NotImplementedError
