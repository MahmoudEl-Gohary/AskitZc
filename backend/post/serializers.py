from rest_framework import serializers
from .models import Post
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at_formated', 'created_by')