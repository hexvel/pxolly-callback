from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.handlers.pxolly.confirmation import handle_confirmation
from app.handlers.pxolly.invite_user import handle_invite_user
from app.handlers.pxolly.sync import handle_sync
from app.schemas.pxolly import PXollyCallback

router = APIRouter(prefix="/receiver")


@router.post("/pxolly/callback")
async def pxolly_callback(data: PXollyCallback):
    if data.type == "confirmation":
        return await handle_confirmation()

    if data.type == "sync":
        return await handle_sync(data)

    if data.type == "invite_user":
        return await handle_invite_user(data)

    return JSONResponse(content={"ok": True, "code": "b6c60110"}, status_code=200)


@router.post("/iris/callback")
async def pxolly_subscribe(request: Request):
    logger.warning(request)
    return JSONResponse(content="b6c60110", status_code=200)
