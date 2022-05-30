from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import routers
from src.config import config_app, load_config, msg_server_start
from src.core import database


def init_app():
    origins = [
        'http://nginx',
        'http://frontend:3000',
        'http://backend:8000',
        'http://0.0.0.0:8000'
        
    ]

    app = FastAPI()
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    
    load_config()
    config_app(app)
    database.create_db()
    
    msg_server_start(app.description, app.version)
    
    routers.init_app(app)
    
    @app.get('/')
    async def root():
        return {'message': 'Hello Bigger Applications!'}

    return app
