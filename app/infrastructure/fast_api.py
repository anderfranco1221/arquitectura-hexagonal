from fastapi import FastAPI
from app.infrastructure.container import Container
from app.infrastructure.handlers import Handlers

def create_app():
    app_fast = FastAPI()
    #* Configuration, the every tool for to use
    app_fast.container = Container()
    #* Iterator for each route
    for handler in Handlers.iterator():
        app_fast.include_router(handler.router)

    return app_fast
