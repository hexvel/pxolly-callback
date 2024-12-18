from typing import Callable, Dict, List, Union

from vkbottle import API

from app.schemas.pxolly import PXollyCallback


class Bot:
    def __init__(self):
        self.command_handlers: Dict[str, Callable] = {}

    def message(self, commands: Union[str, List[str]]):
        if isinstance(commands, str):
            commands = [commands]

        def decorator(func: Callable):
            for command in commands:
                if command not in self.command_handlers:
                    self.command_handlers[command] = func
            return func

        return decorator

    async def handle_event(self, event: PXollyCallback, api: API):
        prefix = event.object.prefix
        command = event.object.message.text.split(prefix)[1].strip()
        handler = self.command_handlers.get(command)

        if handler:
            return await handler(event, api)


bot = Bot()
