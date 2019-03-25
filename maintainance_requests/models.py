from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault, ValidationError


class MaintainanceRequest(models.Model):
    request_title = models.CharField(max_length=100)
    request_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending')
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,related_name="maintenancerequests")

    def __str__(self):
        return self.request_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})