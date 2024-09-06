from django.db import models
from django.contrib.auth.models import User

class ShortLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='short_links')
    original_url = models.URLField(max_length=250)
    short_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"wow/{self.short_code} -> {self.original_url}"

    @property
    def full_short_url(self):
        return f"wow/{self.short_code}"
