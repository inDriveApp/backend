from . import login
from . import user


def init_app(app):
    app.include_router(login.router)
    app.include_router(user.router)
