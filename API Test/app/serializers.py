from rest_framework import serializers
from app.models import Jokes
import hashlib

class JokeSeriazers(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = "__all__"
        
    def validate_joke(self, joke):
        
        joke_hash = hashlib.sha256(joke.strip().lower().encode('utf-8')).hexdigest()
        
        if Jokes.objects.filter(joke_hash=joke_hash).exists():
            raise serializers.ValidationError("This joke already exists.")
        return joke
        