from uuid import UUID
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=10, deprecated="auto")


def is_valid_uuid(uuid: str, version: int = 4) -> bool:
    try:
        uuid_obj = UUID(uuid, version=version)
        return str(uuid_obj) == uuid
    except ValueError:
        return False


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
