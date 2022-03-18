from . import login


def init_app(app):
    app.include_router(login.router)
