#!/bin/bash

uvicorn src.main:init_app \
--reload \
--reload-dir src \
--no-server-header \
--no-date-header \
--factory \
--host 0.0.0.0 \
--port 8000