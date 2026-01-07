#!/bin/bash

source .venv/bin/activate

python -m uvicorn m8flow.app:app --port 7004 --env-file "$(pwd)/.env" --app-dir "$(pwd)"

