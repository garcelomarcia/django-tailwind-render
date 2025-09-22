#!/usr/bin/env bash
set -euo pipefail

pip install -r requirements.txt

# valida configuración de prod (falla el build si algo crítico falta)
python manage.py check --deploy

# sirve estáticos (WhiteNoise)
python manage.py collectstatic --no-input

python manage.py makemigrations

# aplica migraciones que YA vienen comiteadas
python manage.py migrate --no-input