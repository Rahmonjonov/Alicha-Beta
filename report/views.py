from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Checkout
from drf_yasg.utils import swagger_auto_schema
from .serializer import OrderSerializer, CheckoutSerializer, CheckoutCreateSerializer, OrderCreateSerializer
from products.models import Product
from datetime import date

""" Order Function Start """


@api_view(['GET'])
def order_list(request):
    try:
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def order_detail(request, pk):
    try:
        queryset = Order.objects.get(id=pk)
        serializer = OrderSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['POST'], request_body=OrderCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_add(request, pk):
    try:
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id=pk)
        if product.quantity > 0:
            total = product.sel_price * quantity
            Order.objects.create(
                total=total,
                quantity=quantity,
                product_id=product.id,
                user=request.user
            )
            product.quantity -= quantity
            product.save()
            return Response({'Answer': 'Success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Answer': 'Product is not enough'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def order_delete(request, pk):
    try:
        order = Order.objects.get(id=pk)
        product = Product.objects.get(id=order.product.id)
        product.quantity += order.quantity
        product.save()
        order.delete()
        return Response({'Messages': 'Success'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


""" Order Function End """


""" Checkout  Function start"""


@api_view(['GET'])
def checkout_list(request):
    try:
        queryset = Checkout.objects.all()
        serializer = CheckoutSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def checkout_detail(request, pk):
    try:
        queryset = Checkout.objects.get(id=pk)
        serializer = CheckoutSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['post'], request_body=CheckoutCreateSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout_add(request):
    try:
        client = request.POST.get('client')
        type_payment = request.POST.get('type_payment')
        order = Order.objects.all()
        for i in order:
            max_sum = i.quantity
            print(max_sum)
            checkout = Checkout.objects.create(
                total=i.total,
                user=request.user,
                client_id=client,
                type_payment=type_payment,
            )
            checkout.order.set(order)
            checkout.save()
            return Response({'Messages': 'Object Checkout Create'}, status=status.HTTP_201_CREATED)
    except Exception as err:
        return Response({'Messages': err}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def checkout_destroy(request, pk):
    try:
        checkout = Checkout.objects.get(id=pk)
        checkout.delete()
        return Response({'Messages': 'Object Checkout Data Delete'})
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def today_checkout(request):
    try:
        today = date.today()
        checkout = Checkout.objects.filter(date_now=today)
        serializer = CheckoutSerializer(checkout, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception:
        return Response({'Messages': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)

