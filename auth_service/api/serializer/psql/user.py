from rest_framework import serializers
from auth_service.api.models import User


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, include_timestamps=False, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if not include_timestamps:
            self.fields.pop('created_at', None)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = User
        fields = [
            "id",
            "login",
            "password",
            "last_login",
            "created_at",
        ]
