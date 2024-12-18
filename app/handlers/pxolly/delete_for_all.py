from fastapi.responses import JSONResponse
from vkbottle import API

from app.schemas.pxolly import PXollyCallback


async def handle_delete_for_all(data: PXollyCallback, api: API) -> JSONResponse:
    conversation_message_ids = []

    deleted = await api.messages.delete(
        peer_id=data.object.chat_local_id + 2000000000,
        cmids=data.object.conversation_message_ids,
        delete_for_all=1,
    )

    for message in deleted:
        conversation_message_ids.append(message.conversation_message_id)

    return JSONResponse(
        content={"ok": True, "conversation_message_ids": conversation_message_ids},
        status_code=200,
    )
