from rest_framework import serializers

from users.models import OTPRequest


class OTPRequestSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=50, allow_null=False)
    channel = serializers.ChoiceField(allow_null=False, choices=OTPRequest.OTPChannel.choices)


class OTPRequestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ('request_id',)


class VerifyOTPRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False)
    receiver = serializers.CharField(max_length=64, allow_null=False)


class ObtainTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=128, allow_null=False)
    refresh = serializers.CharField(max_length=128, allow_null=False)
    created = serializers.BooleanField()
