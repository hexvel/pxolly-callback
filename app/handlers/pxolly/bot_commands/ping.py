from ping3 import ping
from vkbottle import API

from app.core.emoji import Emoji
from app.handlers.decorator import bot
from app.schemas.pxolly import PXollyCallback


@bot.message(commands=["пинг", "ping"])
async def ping_handler(event: PXollyCallback, api: API):
    ping_result = ping("api.vk.com")
    if ping_result is not None:
        await api.messages.edit(
            peer_id=event.object.chat_local_id + 2000000000,
            message=f"{Emoji.CLOCK} Пинг до API: {ping_result:.3f} сек",
            cmid=event.object.message.conversation_message_id,
        )
    else:
        await api.messages.edit(
            peer_id=event.object.chat_local_id + 2000000000,
            message=f"{Emoji.WARNING} Не удалось получить пинг до VK API",
            cmid=event.object.message.conversation_message_id,
        )

    return {"ok": True}
