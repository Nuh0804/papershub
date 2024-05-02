from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
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
            status=HTTP_200_OK
            )






class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # @action(detail=False, methods=['POST'])
    # def token(self, request):
    #     auth_base_url =  "https://authenticator-sandbox.azampay.co.tz"# Replace with your actual base URL
    #     app_name = "papershub"
    #     client_id = settings.CLIENT_ID 
    #     client_secret = settings.CLIENT_SECRET_KEY

    #     token_data = generate_token(auth_base_url, app_name, client_id, client_secret)
        
    #     data = {
    #         "msg": "payment was successful",
    #         "data": token_data
    #     }
    #     return Response(data)
    

    @action(detail=False, methods=["POST"])
    def pay(self, request):

        #generate token for authorization 
        auth_base_url =  "https://authenticator-sandbox.azampay.co.tz"# Replace with your actual base URL
        app_name = "papershub"
        client_id = settings.CLIENT_ID 
        client_secret = settings.CLIENT_SECRET_KEY

        token_data = generate_token(auth_base_url, app_name, client_id, client_secret)
        # Access the access token
        token = token_data.get('data', {}).get('accessToken', None)

        #payment
        base_url =  "https://sandbox.azampay.co.tz"# Replace with your actual base URL
        api_key = settings.CLIENT_SECRET_KEY
        account_number = "1292-123"
        amount = '2000.0'
        currency = "TZS"
        external_id = "123"
        provider='Tigo'
        additional_properties = {"property1": None, "property2": None}

        payment_data = azampay_mno_checkout(base_url, token, api_key, account_number, amount, currency, external_id, provider, additional_properties)
        
        data = {
            "msg": "payment was successful",
            "data": payment_data
        }
        return Response(data)  