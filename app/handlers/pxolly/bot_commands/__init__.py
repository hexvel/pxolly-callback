import importlib
import os
from pathlib import Path


def load_commands(directory: str = "app.handlers.pxolly.bot_commands"):
    commands_path = Path(directory.replace(".", "/"))

    for file in os.listdir(commands_path):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"{directory}.{file[:-3]}"
            print(module_name)
            importlib.import_module(module_name)
