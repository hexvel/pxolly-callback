import aiohttp


class VKAPIClient:
    def __init__(self, access_token: str | None = None):
        self._access_token = access_token
        self._v = "5.131"
        self._vk_url = "https://api.vk.com/method/"
        self._session = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._session:
            await self._session.close()

    async def get(self, url: str, params: dict = None):
        async with self._session.get(url=url, params=params) as response:
            return await response.json()

    async def post(self, url: str, params: dict = None):
        async with self._session.post(url=url, params=params) as response:
            return await response.json()

    async def execute(self, method: str, params: dict = None):
        params = params or {}
        params.update(access_token=self._access_token, v=self._v)
        async with self._session.get(
            url=self._vk_url + method, params=params
        ) as response:
            return await response.json()
