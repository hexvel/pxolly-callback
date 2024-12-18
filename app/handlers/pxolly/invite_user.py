from fastapi.responses import JSONResponse
from vkbottle import API

from app.core.emoji import Emoji
from app.schemas.pxolly import PXollyCallback


async def handle_invite_user(data: PXollyCallback, api: API) -> JSONResponse:
    await api.messages.add_chat_user(
        chat_id=data.object.chat_local_id,
        user_id=data.object.user_id,
    )

    if data.object.is_expired == 1:
        user = await api.users.get(user_ids=data.object.user_id)

        await api.messages.send(
            chat_id=data.object.chat_local_id,
            random_id=0,
            message=f"{Emoji.OK} Пользователь [id{data.object.user_id}|{user[0].first_name} {user[0].last_name}] разблокирован по истечению срока блокировки.",
        )

    return JSONResponse(content={"ok": True}, status_code=200)
