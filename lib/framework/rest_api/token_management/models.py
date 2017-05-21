from django.conf import settings
from django.db import models


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class RefreshToken(models.Model):
    key = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='refresh_tokens')
    service = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'service')

    def save(self, *args, **kwargs):
        return super(RefreshToken, self).save(*args, **kwargs)

    def __str__(self):
        return self.key
