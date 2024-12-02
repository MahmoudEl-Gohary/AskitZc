import uuid 
from django.db import models
from account.models import User
from django.utils.timesince import timesince

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='posts' ,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
        
    def created_at_formated(self):
        return timesince(self.created_at)
    