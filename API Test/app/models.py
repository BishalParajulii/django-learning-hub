from django.db import models
import hashlib

# Create your models here.
class Jokes(models.Model):
    joke = models.CharField(max_length=255 , unique=True)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    joke_hash = models.CharField(
        max_length=64,
        unique=True,
        editable=False,
        default=''
    )
    
    def save(self, *args, **kwargs):
        normalized_joke = self.joke.strip().lower()
        self.joke_hash = hashlib.sha256(normalized_joke.encode('utf-8')).hexdigest()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.joke

    
