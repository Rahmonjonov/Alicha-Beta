from .models import Client, Employee
from .serializer import ClientSerializer, ClientCreateSerializer, EmployeeSerializer, EmployeeCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from account.models import User
""" Client Function Start """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_list(request):
    try:
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_detail(request, pk):
    try:
        queryset = Client.objects.get(id=pk)
        serializer = ClientSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=ClientCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def client_add(request):
    try:
        data = request.data
        Client.objects.create(
            name=data.get('name'),
            phone=data.get('phone'),
            debt=data.get('debt'),
            date=data.get('date'),
        )
        return Response({"Messages": 'Client Object Data Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def client_change(request, pk):
    try:
        data = request.data
        queryset = Client.objects.get(id=pk)
        queryset.name = data.get('name')
        queryset.phone = data.get('phone')
        queryset.debt = data.get('debt')
        queryset.date = data.get('date')
        queryset.save()
        return Response({'Messages':'Object Client Change Data'}, status=status.HTTP_200_OK)
    except Exception as Er:
        return Response({'Messages': Er}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def client_delete(request, pk):
    try:
        queryset = Client.objects.get(id=pk)
        queryset.delete()
        return Response({'Messages': 'Object Client Delete '}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


""" Client Function End """

""" Employee Function Start """


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def employee_list(request):
    try:
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def employee_detail(request, pk):
    try:
        queryset = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=EmployeeCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def employee_add(request):
    try:
        data = request.data
        Employee.objects.create(
            name=data.get('name'),
            phone=data.get('phone'),
            password=data.get('password')
        )
        User.objects.create_user(username=data.get('phone'), password=data.get('password'), first_name=data.get('name'))
        return Response({"Messages": 'Employee Object Data Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def employee_change(request, pk):
    try:
        data = request.data
        queryset = Employee.objects.get(id=pk)
        user_queryset = User.objects.get(username=queryset.phone)
        user_queryset.first_name = data.get('name')
        user_queryset.username = data.get('phone')
        user_queryset.set_password(data.get('password'))
        queryset.name = data.get('name')
        queryset.phone = data.get('phone')
        queryset.password = data.get('password')
        queryset.save()
        user_queryset.save()
        return Response({'Messages': 'Object Employee Change Data'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def employee_delete(request, pk):
    try:
        queryset = Employee.objects.get(id=pk)
        user_queryset = User.objects.get(username=queryset.phone)
        user_queryset.delete()
        queryset.delete()
        return Response({'Messages': 'Object Employee Delete '}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


""" Employee Function End """

