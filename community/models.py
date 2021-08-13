from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone
# Create your models here.

class Community(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date=models.DateTimeField('date published')
    body=models.TextField(max_length=500)
    hits=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:50]
        
class Reply(models.Model):
    post = models.ForeignKey(Community, related_name='comments', on_delete=models.CASCADE)
    messages=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def approve(self):
        self.save()

    def __str__(self):
        return self.messages