import os 
from types import ModuleType
from typing import Iterator

class Handlers:
    handlers_base_path = ('app', 'infrastructure', 'handlers')
    ignored = ('__init__.py', '__pycache__')

    #get all class of the this folder
    @classmethod
    def __all_module_names(cls) -> list:
        return list(
            filter(
                lambda module: module not in cls.ignored, os.listdir('/'.join(cls.handlers_base_path))
            )
        )

    #Get the name of the class handlers
    @classmethod
    def __module_namespace(cls, handler_name: str) -> str:
        return '%s.%s' % ('.'.join(cls.handlers_base_path), handler_name)

    #Get the file the class handlers
    @classmethod
    def iterator(cls) -> Iterator[ModuleType]:
        for module in cls.__all_module_names():
            import importlib
            handler = importlib.import_module(cls.__module_namespace(module[:-3]))
            yield handler

    @classmethod
    def modules(cls) -> map:
        return map(
                lambda module: cls.__module_namespace(module[:-3]), cls.__all_module_names()
        )