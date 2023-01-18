from .admin import Order
from .serializers import OrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .payment import client, client_receipt
from rest_framework.views import APIView
from main.models import Offer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CardCreate(APIView):
    def post(self, request, *args, **kwargs):
        number = self.request.data.get('number')
        expire = self.request.data.get('expire')
        save = True
        res = client._cards_create(number=number, expire=expire, save=save)
        print(res)
        try:
            token = res['result']['card']['token']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_400_BAD_REQUEST)
        resp = client._card_get_verify_code(token)
        return Response({'message': 'Verification code has sent', 'token': token}, status=status.HTTP_200_OK)


class CardVerify(APIView):
    def post(self, request, *args, **kwargs):
        verify_code = self.request.data.get('verify_code')
        token = self.request.data.get('token')
        res = client._cards_verify(verify_code, token)
        print(res)
        try:
            token = res['result']['card']['token']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_404_NOT_FOUND)
        check = client._cards_check(token)
        return Response(str(check), status=status.HTTP_200_OK)


class ReceiptCreate(APIView):
    def post(self, request, *args, **kwargs):
        offer_id = self.request.data.get('offer_id')
        offer = Offer.objects.filter(id=offer_id).first()
        if not offer:
            return Response({'message': 'Invalid Offer ID'})
        amount = offer.price
        pk = self.request.data.get('order_id')
        order_tour = Order.objects.filter(id=pk).first()
        if not order_tour:
            return Response({'message': 'Invalid order'}, status=status.HTTP_404_NOT_FOUND)
        token = self.request.data.get('token')
        phone = '998977165434'
        res = client_receipt._receipts_create(123, amount, f'{order_tour.id}', title=order_tour.name, code='21331213',
                                              package_code='123456', price=order_tour.price)
        print(res)
        try:
            invoice_id = res['result']['receipt']['_id']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_404_NOT_FOUND)
        try:
            pay = client_receipt._receipts_pay(123, invoice_id, token, phone)
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_400_BAD_REQUEST)
        order_tour.is_paid = True
        order_tour.save()
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)
