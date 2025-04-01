from datetime import  datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
from decouple import config
from jose import JWTError, jwt

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthServiceException(Exception):
    pass
class InvalidCredentials(Exception):
    pass

class AuthService:

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        try:
            if not pwd_context.verify(plain_password, hashed_password):
                raise InvalidCredentials("Incorrect password")
            return True
        except ValueError as e:
            raise AuthServiceException(f"Error while verifying the password: {e}")
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
        to_encode.update({"exp": expire})
        try:
            encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        except JWTError as e:
            raise AuthServiceException(f"Error while encoding jwt: {e}")
        return encoded_jwt
