from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from django.contrib.auth import logout, authenticate, login
from rest_framework import status
from .token import get_tokens_for_user
from .serializer import LoginSerializer, UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST'])
def sign_in(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            user_get = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                data = {
                        'id': user_get.id,
                        'username': username,
                        'limit': user_get.limit,
                        'first_name': user_get.first_name,
                        'used_limit': user_get.used_limit,
                        'admin': user_get.is_superuser,
                        'token': token,
                                    }
                login(request, user)
                return Response(data, status.HTTP_200_OK)
            else:
                return Response({'message': 'Username or password is incorrect !'}, status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=400, data={'error': serializer.errors})
    except Exception:
         return Response({'Messages': 'Error'}, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=UserCreateSerializer)
@api_view(['POST'])
def sign_up(request):
    try:
        data = request.data
        user = User.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            phone_model=data.get('phone_model'),
            limit=data.get('limit'),
            shop_name=data.get('shop_name'),
            first_name=data.get('first_name')

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return Response({"Messages": 'Success'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def user_logout(request):
    try:
        logout(request)
        return Response({"Messages": 'Success'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'Error messages'}, status=status.HTTP_400_BAD_REQUEST)

