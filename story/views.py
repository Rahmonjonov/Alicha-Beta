from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Cost, DebtMarket, StoreAbout
from .serializer import StoreAboutSerializer, CostSerializer, DebtMarketSerializer, StoreAboutCreateSerializer, DebtMarketCreateSerializer, CostCreateSerializer
from drf_yasg.utils import swagger_auto_schema

""" Story About Function Start """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def story_about_list(request):
    try:
        queryset = StoreAbout.objects.all()
        serializer = StoreAboutSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def story_about_detail(request, pk):
    try:
        queryset = StoreAbout.objects.get(id=pk)
        serializer = StoreAboutSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=StoreAboutCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def story_about_add(request):
    try:
        data = request.data
        StoreAbout.objects.create(
            name=data.get('name'),
            plastic_number=data.get('plastic_number'),
            address=data.get('address'),
        )
        return Response({"Messages": 'Story About Object Data Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def story_about_change(request, pk):
    try:
        data = request.data
        story = StoreAbout.objects.get(id=pk)
        story.name = data.get('name'),
        story.plastic_number = data.get('plastic_number'),
        story.address = data.get('address'),
        story.save()
        return Response({"Messages": 'Story About Object Data Change'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def story_about_delete(request, pk):
    try:
        queryset = StoreAbout.objects.get(id=pk)
        queryset.delete()
        return Response({"Messages": 'Story About Object Data Delete'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


"""  Story About Function End """

""" Dept Market Function Start """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dept_market_list(request):
    try:
        queryset = DebtMarket.objects.all()
        serializer = DebtMarketSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dept_market_detail(request, pk):
    try:
        queryset = DebtMarket.objects.get(id=pk)
        serializer = DebtMarketSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=StoreAboutCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dept_market_add(request):
    try:
        data = request.data
        DebtMarket.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            deadline=data.get('deadline'),
            date=data.get('date'),
        )
        return Response({"Messages": 'Dept Market Object Data Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def dept_market_change(request, pk):
    try:
        data = request.data
        dept = DebtMarket.objects.get(id=pk)
        dept.name = data.get('name')
        dept.price = data.get('price')
        dept.deadline = data.get('deadline')
        dept.date = data.get('date')
        dept.save()
        return Response({"Messages": 'Dept Market Object Data Change'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dept_market_delete(request, pk):
    try:
        queryset = DebtMarket.objects.get(id=pk)
        queryset.delete()
        return Response({"Messages": 'Dept Market Object Data Delete'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


"""  Dept Market Function End """


""" Dept Market Function Start """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cost_list(request):
    try:
        queryset = Cost.objects.all()
        serializer = CostSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cost_detail(request, pk):
    try:
        queryset = Cost.objects.get(id=pk)
        serializer = CostSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=StoreAboutCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cost_add(request):
    try:
        data = request.data
        Cost.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            extra=data.get('extra'),
            date=data.get('date'),
        )
        return Response({"Messages": 'Cost Object Data Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def cost_change(request, pk):
    try:
        data = request.data
        cost = Cost.objects.get(id=pk)
        cost.name = data.get('name')
        cost.price = data.get('price')
        cost.extra = data.get('extra')
        cost.date = data.get('date')
        cost.save()
        return Response({"Messages": 'Cost Object Data Change'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cost_delete(request, pk):
    try:
        queryset = Cost.objects.get(id=pk)
        queryset.delete()
        return Response({"Messages": 'Cost Objects  Data Delete'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


"""  Cost Function End """