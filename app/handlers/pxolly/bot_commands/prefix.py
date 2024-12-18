from vkbottle import API

from app.core.emoji import Emoji
from app.core.settings import get_pxolly_settings
from app.handlers.decorator import bot
from app.schemas.pxolly import PXollyCallback


@bot.message(commands=["префикс", "prefix"])
async def prefix_handler(event: PXollyCallback, api: API):
    prefix = event.object.message.text.split()

    if len(prefix) <= 2:
        await api.messages.edit(
            peer_id=event.object.chat_local_id + 2000000000,
            message=f"{Emoji.OK} Ваш префикс: {prefix[0]}",
            cmid=event.object.message.conversation_message_id,
        )
        return {"ok": True}

    if len(prefix[2].strip()) < 2:
        await api.messages.edit(
            peer_id=event.object.chat_local_id + 2000000000,
            message=f"{Emoji.WARNING} Префикс не может быть короче 2 символов.",
            cmid=event.object.message.conversation_message_id,
        )
        return {"ok": True}

    await api.http_client.request_json(
        url="https://api.pxolly.ru/m/callback.setBotPrefix",
        method="POST",
        params={
            "access_token": get_pxolly_settings()["api_token"],
            "prefix": prefix[2].strip(),
        },
    )

    await api.messages.edit(
        peer_id=event.object.chat_local_id + 2000000000,
        message=f"{Emoji.OK} Префикс обновлён на: {prefix[2].strip()}.",
        cmid=event.object.message.conversation_message_id,
    )
    return {"ok": True}
