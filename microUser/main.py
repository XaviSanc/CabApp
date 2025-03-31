from contextlib import asynccontextmanager
from fastapi import APIRouter, Depends, FastAPI
import uvicorn
from loguru import logger
from infrastructure.database.Postresql import PostgreSQL, get_db, initialize_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    try:
        await PostgreSQL.connect()
        await initialize_database()
        yield
        await PostgreSQL.close()
    except Exception as e:
        logger.error(
            f"Exception raised while initializing database {e}"
        )


app = FastAPI(
    title="microUser",
    docs_url="/docs",
    lifespan=lifespan
)

router = APIRouter(prefix="/api")

@router.get("/test")
async def get_things(db=Depends(get_db)):
    query = "SELECT * FROM passenger.test;" 
    results = await db.fetch(query)
    return {"data": results}


@router.get("/health")
def health_check():
    return {"message": "I'm alive"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
