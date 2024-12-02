from .models import Post
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from .forms import PostForm
from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def post_list_profile(request, id):
    posts = Post.objects.filter(created_by=id)
    user = User.objects.get(pk=id)
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse({
        'user': user_serializer.data,
        'posts': post_serializer.data
    }, safe=False)

@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid data'})
    
