#!/bin/bash

# Create virtual environment if it doesn't exist
[ -d .venv ] || python3 -m venv .venv

source .venv/bin/activate

export PYTHONPATH=/mnt/c/dev/repos/poc-m8flow-patching/upstream/spiffworkflow-backend:$PYTHONPATH
export PYTHONPATH=/mnt/c/dev/repos/poc-m8flow-patching/upstream/spiffworkflow-backend/src:$PYTHONPATH

cd /mnt/c/dev/repos/poc-m8flow-patching/upstream/spiffworkflow-backend
uv sync --all-groups --active
cd -


python -m uvicorn m8flow.app:app --port 7004 --env-file "$(pwd)/.env" --app-dir "$(pwd)"

