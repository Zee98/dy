from django.db import models

class Sms(models.Model):
    name            = models.CharField(max_length=150, null=True, blank=True)
    email         = models.EmailField(null=True, blank=True)
    message      = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

