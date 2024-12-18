from vkbottle import API

from app.core.settings import get_vk_token

vk_api = API(get_vk_token())


def get_vk_api() -> API:
    return vk_api
