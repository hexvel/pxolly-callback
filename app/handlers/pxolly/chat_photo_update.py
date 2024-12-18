from aiohttp import ClientSession, FormData
from fastapi.responses import JSONResponse
from vkbottle import API

from app.schemas.pxolly import PXollyCallback


async def chat_photo_update_handler(data: PXollyCallback, api: API) -> JSONResponse:
    upload = await api.request(
        "photos.getChatUploadServer", dict(chat_id=data.object.chat_local_id)
    )
    upload_url = upload["response"]["upload_url"]

    async with ClientSession() as session:
        async with session.get(data.object.photo_url) as photo_resp:
            photo_data = await photo_resp.read()

        form_data = FormData()
        form_data.add_field(
            "file", photo_data, filename="photo.jpg", content_type="image/jpeg"
        )

        async with session.post(upload_url, data=form_data) as response:
            response_data = await response.json()
            await api.messages.set_chat_photo(file=response_data["response"])

    return JSONResponse(content={"ok": True}, status_code=200)
