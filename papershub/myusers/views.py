from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import OrderSerializer
from .models import Order
from .payment_functions import azampay_mno_checkout, generate_token

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        access_token= response.data['access']
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.user
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=access_token,
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )
        return Response({
            **serializer.validated_data,
            **{
                "email": user.email,
                "program": str(user.degree_program),
                "year": user.year,
                }
            },
            status=status.HTTP_200_OK
            )



class OrderViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer   
    

    @action(detail=False, methods=["POST"])
    def pay(self, request):
        user = self.request.user
        data = request.data

        # Generate token for authorization
        auth_base_url = settings.AUTH_BASE_URL  
        app_name = settings.APP_NAME
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET_KEY

        try:
            token_data = generate_token(auth_base_url, app_name, client_id, client_secret)
            token = token_data.get('data', {}).get('accessToken', None)
            print(token)

            if not token:
                return Response({"error": "Failed to generate access token"}, status=status.HTTP_400_BAD_REQUEST)

            # Payment
            account_number = data["phone_number"]
            provider = data["provider"]
            base_url = settings.BASE_URL 
            api_key = settings.CLIENT_SECRET_KEY
            amount = '2000.0'
            currency = "TZS"
            external_id = "123"

            payment_data = azampay_mno_checkout(base_url, token, api_key, account_number, amount, currency, external_id, provider)

            if not payment_data:  # Check if payment_data is None
                return Response({"error": "Payment processing failed"}, status=status.HTTP_400_BAD_REQUEST)

            transaction_id = payment_data.get('transactionId')

            if not transaction_id:
                return Response({"error": "Payment processing failed"}, status=status.HTTP_400_BAD_REQUEST)

            # Order creation and successful response
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(transaction_id=transaction_id, user=user, pending_status = "C")
                return Response({
                    "msg": "payment was successful",
                    "data": payment_data
                })

        except Exception as e:  # Catch any unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 