from fastapi.responses import JSONResponse
from vkbottle import API

from app.core.settings import get_pxolly_settings, set_pxolly_code


async def handle_confirmation(api: API) -> JSONResponse:
    pxolly_code = await api.http_client.request_json(
        url="https://api.pxolly.ru/m/callback.getConfirmationCode",
        method="POST",
        params={"access_token": get_pxolly_settings()["api_token"]},
    )

    set_pxolly_code(pxolly_code["response"]["code"])
    return JSONResponse(
        content={"ok": True, "code": pxolly_code["response"]["code"]},
        status_code=200,
    )
