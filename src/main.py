from fastapi import FastAPI

from src.api import routers
from src.config import config_app, load_config, msg_server_start
from src.core import database


def init_app():

    app = FastAPI()
    
    load_config()
    config_app(app)
    database.create_db()
    
    msg_server_start(app.description, app.version)
    
    routers.init_app(app)
    
    @app.get("/")
    async def root():
        return {"message": "Hello Bigger Applications!"}

    return app
