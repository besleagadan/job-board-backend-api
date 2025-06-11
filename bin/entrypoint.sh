#!/bin/bash
set -e

echo "Starting server..."
exec uv run manage.py runserver 0.0.0.0:8000
