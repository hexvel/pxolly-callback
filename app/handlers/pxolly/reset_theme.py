from fastapi.responses import JSONResponse
from vkbottle import API

from app.schemas.pxolly import PXollyCallback


async def reset_theme_handler(data: PXollyCallback, api: API) -> JSONResponse:
    await api.request(
        "messages.resetConversationStyle",
        data={"peer_id": data.object.chat_local_id + 2000000000},
    )

    return JSONResponse(content={"ok": True}, status_code=200)
