import os
from os.path import exists

import dotenv # from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.core import database
from src.version import __version__


def msg_server_start(msg, versao):
    spaces=len(msg) - len(versao) - 5
    print(
        '\n', '#' * (len(msg) + 6),
        '\n## ', ' ' * len(msg), ' ##',
        '\n## ', msg, ' ##',
        '\n## ', ' ' * len(msg), ' ##',
        '\n', '#' * (len(msg) + 6), '\n',
        ' ' * spaces, 'version: ', versao, '\n',
        sep=''
    )


def load_config():
    if not exists('../.env'):
        print('\n\033[0m\033[31mERROR', end='')
        print('\033[0m:    Environment file not found\n')
        uvicorn.Server.shutdown()  
    
    dotenv.load_dotenv('../.env')


def config_app(app):
    methods = ["POST", "GET", "PUT", "DELETE", "PATCH"]
    
    app.title = 'InDrive'
    app.version = __version__
    app.description = 'InDrive app'
    
    app.router.redirect_slashes = False  # TODO Verificar comportamento padrão
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=methods,
        # allow_headers=headers,
        expose_headers="x-version"
    )
    
    database.APP_NAME = app.title
