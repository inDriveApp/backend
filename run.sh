#!/bin/bash

uvicorn main:app \
--reload \
--no-server-header \
--no-date-header \
--host 0.0.0.0 \
--port 8000
