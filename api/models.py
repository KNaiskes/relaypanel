from django.db import models

class Relay(models.Model):
    name = models.CharField(max_length=30, unique=True)
    device = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
