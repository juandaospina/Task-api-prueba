from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# ENVIRONMENT
APP_ENV = "development"
FLASK_ENV = APP_ENV
FLASK_DEBUG = True
DEBUG = True

# APP
JSON_AS_ASCII = False
PROPAGATE_EXCEPTIONS = True
ERROR_404_HELP = False