from typing import Optional
import datetime, jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from auth_service.api.consumer.utils.env import get_env_variable
from auth_service.api.consumer.repository.psql.user.one import one_user_by_login_password_psql, one_user_psql
from auth_service.api.consumer.data.repository.psql.user.one import RepositoryOneUserByLoginPasswordInput
from auth_service.api.consumer.data.response import Error


class JWTBasicAuthenticationMiddleware(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise AuthenticationFailed("You did not provide authorization headers.")
        try:
            token = auth_header.split(" ")[1]
            is_valid = self.decode_jwt(token)
            if not is_valid:
                return False
            return True

        except IndexError:
            raise AuthenticationFailed("Bearer token not provided.")

    def decode_jwt(self, token: str):
        try:
            payload = jwt.decode(
                token,
                get_env_variable("TOKEN_KEY"),
                algorithms=[get_env_variable("TOKEN_ALGORITHM")]
            )

            payload_user = payload.get("user")
            user, raw_error, is_valid, status_code = one_user_psql(payload_user['id'])
            if not is_valid:
                error: Error = raw_error
                raise AuthenticationFailed(error)
            return True

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.DecodeError as e:
            raise AuthenticationFailed("Token decode error.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")

    def encode_jwt(self, login: str, password: str) -> tuple[Optional[str], Optional[Error], bool, int]:
        payload_one: RepositoryOneUserByLoginPasswordInput = {
            'login': login,
            'password': password
        }
        output, error, is_valid, status_code = one_user_by_login_password_psql(payload_one)
        if not is_valid:
            return output, error, is_valid, status_code

        expired = datetime.datetime.utcnow() + datetime.timedelta(hours=10)

        payload = {
            "user": output,
            "exp": expired,
            "iat": datetime.datetime.utcnow()
        }

        token: str = jwt.encode(payload, get_env_variable("TOKEN_KEY"), algorithm=get_env_variable("TOKEN_ALGORITHM"))
        return token, error, is_valid, status_code
