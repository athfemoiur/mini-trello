import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from users.sender import send_otp
from users.utils import generate_otp_password


class User(AbstractUser):
    pass


class OTPRequestManager(models.Manager):
    def generate(self, data):
        otp = self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp

    def is_valid(self, data):
        current_time = timezone.now()
        return self.get_queryset().filter(receiver=data['receiver'], request_id=data['request_id'],
                                          password=data['password'], created__lt=current_time,
                                          created__gt=current_time - timedelta(minutes=2)).exists()


class OTPRequest(models.Model):
    class OTPChannel(models.TextChoices):
        PHONE = 'phone'
        EMAIL = 'email'

    objects = OTPRequestManager()

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    channel = models.CharField(max_length=10, choices=OTPChannel.choices, default=OTPChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp_password)
    created = models.DateTimeField(auto_now_add=True, editable=False)
