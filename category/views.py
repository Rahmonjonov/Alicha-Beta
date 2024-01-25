from .models import Category
from .serializer import CategorySerializer, CategoryCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_list(request):
    try:
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=CategoryCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def category_add(request):
    try:
        data = request.data
        Category.objects.create(
            name=data.get('name'),
            image=data.get('image'),
        )
        return Response({'Messages': 'Object Category Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def category_change(request, pk):
    try:
        data = request.data
        queryset = Category.objects.get(id=pk)
        queryset.name = data.get('name')
        if data.get('image') is not None:
            queryset.image = data.get('image')
        queryset.save()
        return Response({'Messages': 'Object Category Change Data'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def category_delete(request, pk):
    try:
        queryset = Category.objects.get(id=pk)
        queryset.delete()
        return Response({'Messages': 'Object Category Delete'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)