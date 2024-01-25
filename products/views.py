from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import ProductSerializer, ProductCreateSerializer, ProductFileterCategorySerializer, ProductFileterBarcodesSerializer
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products_list(request):
    try:
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products_detail(request, pk):
    try:
        queryset = Product.objects.get(id=pk)
        serializer = ProductSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)

    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=ProductCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def products_add(request):
    try:
        data = request.data
        Product.objects.create(
            product_name=data.get('product_name'),
            barcodes=data.get('barcodes'),
            purchase_price=data.get('purchase_price'),
            sel_price=data.get('sel_price'),
            quantity=data.get('quantity'),
            image=data.get('image'),
            category_id=data.get('category_id'),
        )
        return Response({'Messages': 'Object Product Create'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def products_change(request, pk):
    try:
        data = request.data
        product = Product.objects.get(id=pk)
        product.product_name = data.get('product_name')
        product.barcodes = data.get('barcodes')
        product.purchase_price = data.get('purchase_price')
        product.sel_price = data.get('sel_price')
        product.category_id = data.get('category_id')
        product.quantity = data.get('quantity')
        if data.get('image') is not None:
            product.image = data.get('image')
        product.save()
        return Response({'Messages': 'Object Product Change Data'}, status=status.HTTP_200_OK)
    except Exception as ee:
        return Response({'Data': ee}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def products_delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'Messages': 'Object Product Delete'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'data': 'error messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['post'], request_body=ProductFileterCategorySerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_filter_category(request):
    try:
        data = request.data
        product = Product.objects.filter(category=data.get('category'))
        serializer = ProductSerializer(product, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['post'], request_body=ProductFileterBarcodesSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_filter_barcodes(request):
    try:

        if request.method == 'POST':
            barcodes = request.POST.get('barcodes')
            product = Product.objects.get(barcodes=barcodes)
            if product:
                serializer = ProductSerializer(product).data
                return Response(serializer, status=status.HTTP_200_OK)
            else:
                return Response({'Messages': 'Product is not available'})
        else:
            return Response({'Data': 'Error request method'}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception:
        return Response({'Data': 'Error Messages'}, status=status.HTTP_401_UNAUTHORIZED)

