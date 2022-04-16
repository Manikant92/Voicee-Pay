from django.db import models


class UssdSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_input = models.TextField()

    def __str__(self) -> str:
        return f"{self.user_phone}"
