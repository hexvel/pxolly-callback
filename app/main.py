from fastapi import FastAPI

from app.api.v1.receiver import router as receiver_router


async def lifespan(app: FastAPI) -> None:
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(receiver_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
