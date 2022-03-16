from fastapi import FastAPI

from src.config import config_app, load_config, msg_server_start


def init_app():
    
    load_config()
    app = FastAPI()
    config_app(app)
    
    msg_server_start(app.description, app.version)
    
    routers.init_app(app)
    
    @app.get("/")
    async def root():
        return {"message": "Hello Bigger Applications!"}

    return app
