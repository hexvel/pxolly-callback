from fastapi.responses import JSONResponse
from vkbottle import API

from app.schemas.pxolly import PXollyCallback


async def set_theme_handler(data: PXollyCallback, api: API) -> JSONResponse:
    style = data.object.style

    await api.request(
        "messages.setConversationStyle",
        data={
            "peer_id": data.object.chat_local_id + 2000000000,
            "style": style,
        },
    )
    return JSONResponse(content={"ok": True}, status_code=200)
