import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(name_env: str, default: str = None) -> str:
    from auth_service.api.config.api_config import ENV_MODE, ENV_PATH
    env_file_path = ENV_PATH / f'{ENV_MODE}.env'
    load_dotenv(env_file_path)

    value = os.getenv(name_env)

    if value is not None:
        return value

    if default is not None:
        return default

    raise ImproperlyConfigured(f"Missing required environment variable: {name_env}, {env_file_path}")
