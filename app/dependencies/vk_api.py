from vkbottle import API

from app.core.settings import get_vk_token

vk_api = API(get_vk_token())
vk_api.API_VERSION = "5.228"


def get_vk_api() -> API:
    return vk_api
