from pathlib import Path

# local, dev, prod
ENV_MODE = 'local'

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Media
HOME_FILES = BASE_DIR / 'consumer' / 'media' / 'home'
