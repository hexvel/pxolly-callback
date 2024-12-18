from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from loguru import logger
from vkbottle import API

from app.dependencies.vk_api import get_vk_api
from app.handlers.pxolly.confirmation import handle_confirmation
from app.handlers.pxolly.invite_user import handle_invite_user
from app.handlers.pxolly.sync import handle_sync
from app.schemas.pxolly import PXollyCallback

router = APIRouter(prefix="/receiver")


@router.post("/pxolly/callback", response_model=None)
async def pxolly_callback(
    data: PXollyCallback, api: API = Depends(get_vk_api)
) -> JSONResponse:
    if data.type == "confirmation":
        return await handle_confirmation(api)

    if data.type == "sync":
        return await handle_sync(data, api)

    if data.type == "invite_user":
        return await handle_invite_user(data, api)

    return JSONResponse(content={"ok": True, "code": "b6c60110"}, status_code=200)


@router.post("/iris/callback", response_model=None)
async def pxolly_subscribe(request: Request) -> JSONResponse:
    logger.warning(request)
    return JSONResponse(content="b6c60110", status_code=200)
