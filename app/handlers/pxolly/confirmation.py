from fastapi.responses import JSONResponse

from app.core.settings import get_pxolly_settings, set_pxolly_code
from app.http import VKAPIClient


async def handle_confirmation() -> JSONResponse:
    async with VKAPIClient() as api:
        pxolly_code = await api.post(
            url="https://api.pxolly.ru/m/callback.getConfirmationCode",
            params={"access_token": get_pxolly_settings()["api_token"]},
        )

        set_pxolly_code(pxolly_code["response"]["code"])
        return JSONResponse(
            content={"ok": True, "code": pxolly_code["response"]["code"]},
            status_code=200,
        )
