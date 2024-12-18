import json

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    VK_TOKEN: str
    PXOLLY_API_TOKEN: str
    PXOLLY_SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


def get_pxolly_settings() -> dict:
    with open("app/settings.json", "r", encoding="utf-8") as f:
        return json.load(f)["pxolly"]


def get_vk_token() -> str:
    with open("app/settings.json", "r", encoding="utf-8") as f:
        return json.load(f)["access_token"]


def set_vk_token(token: str) -> None:
    with open("app/settings.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["access_token"] = token
    with open("app/settings.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def set_pxolly_token(token: str) -> None:
    with open("app/settings.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["pxolly"]["api_token"] = token
    with open("app/settings.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def set_pxolly_code(code: str) -> None:
    with open("app/settings.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["pxolly"]["secret_key"] = code
    with open("app/settings.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
