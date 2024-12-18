from fastapi import FastAPI
from loguru import logger

from app.api.v1.receiver import router as receiver_router
from app.handlers.pxolly.bot_commands import load_commands

logger.disable("vkbottle")


async def lifespan(app: FastAPI) -> None:
    load_commands()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(receiver_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
