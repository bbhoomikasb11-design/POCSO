#!/bin/bash
set -e

# Shield 360 - Django Start Script (serves HTML + API)

echo "🚀 Starting Shield 360 (Django)..."

cd "$(dirname "$0")/shield360-django"

if [ ! -d ".venv" ]; then
  echo "🧰 Creating virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "📦 Installing dependencies (if needed)..."
pip install --upgrade pip >/dev/null
pip install -r requirements.txt >/dev/null

echo "🗄️  Applying migrations..."
python manage.py migrate

echo "🌐 Running server at http://localhost:5000"
PORT=5000 python manage.py runserver 0.0.0.0:5000


