from typing import Optional
from api.worker.models.user import User
from api.worker.serializer.psql.user import UserSerializer
from api.worker.consumer.data.response import Error
from worker.consumer.data.repository.psql.user.one import RepositoryOneUserByLoginPasswordInput, \
    RepositoryOneUserByLoginPasswordOutput
from api.worker.consumer.helper.validators import verify_password, get_password_hash


def one_user_by_login_password_psql(payload: RepositoryOneUserByLoginPasswordInput) -> tuple[
    Optional[RepositoryOneUserByLoginPasswordOutput], Optional[Error], bool, int]:
    try:
        login: str = payload['login']
        password: str = payload['password']

        row_user = User.objects.filter(login=login).first()
        if not row_user:
            return None, Error(message=f"Not found user with this login={login}.", type_module="user",
                               type_error="not_found"), False, 400

        if not verify_password(password, row_user.password):
            return None, Error(message="Password is not valid for this user.", type_module="user",
                               type_error="not_valid"), False, 400

        serializer = UserSerializer(row_user).data
        return serializer, None, True, 200

    except Exception as e:
        return None, Error(message=f"one_user_by_login_password_error: {e}.", type_module="user",
                           type_error="not_valid"), False, 417


def one_user_psql(user_id) -> tuple[Optional[RepositoryOneUserByLoginPasswordOutput], Optional[Error], bool, int]:
    try:
        row_user = User.objects.filter(id=user_id).first()
        if not row_user:
            return None, Error(message=f"Not found user with this id={user_id}.", type_module="user",
                               type_error="not_found"), False, 400

        serializer = UserSerializer(row_user).data
        return serializer, None, True, 200

    except Exception as e:
        return None, Error(message=f"one_user_psql_error: {e}.", type_module="user",
                           type_error="not_valid"), False, 417
