from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
        ordering = ['-datetime_created']

    name = models.CharField(max_length=100, null=False)
    rating = models.IntegerField(default=0, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500, null=False)
    email = models.EmailField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
