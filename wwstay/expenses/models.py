from __future__ import unicode_literals

import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    user = models.ForeignKey(User, default=None, related_name='user_expenses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default=os.path.join(settings.BASE_DIR, 'images/xrSh9Z0.jpg'))

    def get_image_path(self):
        return '/static/' + os.path.basename(self.image.url)

    def get_image_path_with_html(self):
        return '<img src="{}" style="max-width:50px;max-height:50px;">'.format(self.get_image_path())
