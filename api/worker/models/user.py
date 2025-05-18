from django.db import models

from worker.consumer.common.generate import generate_uuid


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=generate_uuid, editable=False)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return (
            f"<User(id={self.id}, login={self.login}, password={self.password},"
            f"last_login={self.last_login}, created_at={self.created_at})>"
        )
