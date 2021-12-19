from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import OTPRequest
from users.serializers import OTPRequestSerializer, OTPRequestResponseSerializer, ObtainTokenSerializer, \
    VerifyOTPRequestSerializer

User = get_user_model()


class OTPView(APIView):
    def get(self, request):
        serializer = OTPRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        otp = OTPRequest.objects.generate(data)
        return Response(data=OTPRequestResponseSerializer(otp).data)

    def post(self, request):
        serializer = VerifyOTPRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if OTPRequest.objects.is_valid(data):
            return Response(self._handle_login(data))
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def _handle_login(otp):
        qs = User.objects.filter(username=otp['receiver'])
        if qs.exists():
            created = False
            user = qs.first()
        else:
            created = True
            user = User.objects.create(username=otp['receiver'])

        refresh = RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created': created
        }).data
