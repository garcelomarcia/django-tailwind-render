#!/usr/bin/env python
import os
import sys
from pathlib import Path

def load_dotenv(path: Path):
    """Carga KEY=VALUE desde .env y sobrescribe el entorno local."""
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                os.environ[k] = v
    except FileNotFoundError:
        pass

def main():
    # Carga .env ubicado junto a manage.py
    load_dotenv(Path(__file__).resolve().parent / ".env")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_proj.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
