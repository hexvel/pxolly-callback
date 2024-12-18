from fastapi.responses import JSONResponse
from loguru import logger
from vkbottle import API

from app.core.helpers import search_peer
from app.schemas.pxolly import PXollyCallback


async def handle_sync(data: PXollyCallback, api: API) -> JSONResponse:
    peer = await search_peer(
        api=api,
        text=data.object.message.text,
        from_id=data.object.message.from_id,
        date=data.object.message.date,
        conversation_message_id=data.object.message.conversation_message_id,
    )
    if peer:
        return JSONResponse(
            content={"ok": True, "local_id": peer["response"]}, status_code=200
        )

    return JSONResponse(content={"ok": False}, status_code=400)
