from typing import Optional

from pydantic import BaseModel, Field


class PXollyCallbackUser(BaseModel):
    id: Optional[int] = Field(
        default=None,
    )
    name: Optional[str] = Field(
        default=None,
    )
    role: Optional[int] = Field(
        default=None,
    )


class PXollyCallbackMessage(BaseModel):
    date: Optional[int] = Field(
        default=None,
    )
    conversation_message_id: Optional[int] = Field(
        default=None,
    )
    from_id: Optional[int] = Field(
        default=None,
    )
    text: Optional[str] = Field(
        default=None,
    )


class PXollyCallbackObject(BaseModel):
    date: Optional[int] = Field(
        default=None,
    )
    chat_local_id: Optional[int] = Field(
        default=None,
    )
    from_id: Optional[int] = Field(
        default=None,
    )
    user_id: Optional[int] = Field(
        default=None,
    )
    is_expired: Optional[int] = Field(
        default=None,
    )
    chat_uid: Optional[str] = Field(
        default=None,
    )
    prefix: Optional[str] = Field(
        default=None,
    )
    chat_id: Optional[str] = Field(
        default=None,
    )
    owner_id: Optional[int] = Field(
        default=None,
    )
    user: Optional[PXollyCallbackUser] = Field(
        default=None,
    )
    message: Optional[PXollyCallbackMessage] = Field(
        default=None,
    )
    payload: Optional[str] = Field(
        default=None,
    )


class PXollyCallbackBase(BaseModel):
    type: str
    object: Optional[PXollyCallbackObject] = Field(
        default=None,
    )
    from_id: Optional[int] = Field(
        default=None,
    )
    event_id: Optional[str] = Field(
        default=None,
    )


class PXollyCallback(PXollyCallbackBase):
    pass
