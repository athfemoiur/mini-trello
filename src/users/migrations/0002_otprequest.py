# Generated by Django 3.2.8 on 2021-12-19 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPRequest',
            fields=[
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('channel', models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], default='phone', max_length=10)),
                ('receiver', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
