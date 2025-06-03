from pathlib import Path

# local, dev, prod
ENV_MODE = 'dev'

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / 'env'

# Media
HOME_FILES = BASE_DIR / 'consumer' / 'media' / 'home'
