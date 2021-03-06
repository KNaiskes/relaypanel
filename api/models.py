from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Relay(models.Model):
    name = models.CharField(max_length=30, unique=True)
    device = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
