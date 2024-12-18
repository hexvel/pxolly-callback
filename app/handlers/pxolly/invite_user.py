from fastapi.responses import JSONResponse

from app.core.settings import get_vk_token
from app.http import VKAPIClient
from app.schemas.pxolly import PXollyCallback


async def handle_invite_user(data: PXollyCallback) -> JSONResponse:
    async with VKAPIClient(get_vk_token()) as api:
        await api.execute(
            method="messages.addChatUser",
            params={
                "chat_id": data.object.chat_local_id,
                "user_id": data.object.user_id,
            },
        )

        if data.object.is_expired == 1:
            user = await api.execute(
                method="users.get",
                params={
                    "user_ids": data.object.user_id,
                },
            )

            response = user["response"]
            await api.execute(
                method="messages.send",
                params={
                    "chat_id": data.object.chat_local_id,
                    "message": f"Пользователь [id{data.object.user_id}|{response[0]['first_name']}] разблокирован по истечению срока блокировки.",
                    "random_id": 0,
                },
            )
    return JSONResponse(content={"ok": True}, status_code=200)
