from .forms import SignupForm
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'bio': request.user.bio,
        'description': request.user.description,
    })
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message})