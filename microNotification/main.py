from fastapi import APIRouter, FastAPI
import uvicorn


app = FastAPI(
    title="microNotification",
    docs_url="/docs",
)

router = APIRouter(prefix="/api")


@router.get("/health")
def health_check():
    return {"message": "I'm alive"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004)
