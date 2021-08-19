from celery import shared_task
from django_celery_beat.models import PeriodicTask
from .models import Nonce, JwtToken
from datetime import datetime, timedelta
from django.utils import timezone


@shared_task(bind=True)
def delete_old_nonce_and_token(self):
    Nonce.objects.filter(created_date__lte=datetime.now()-timedelta(hours=24)).delete()
    JwtToken.objects.filter(created_date__lte=timezone.now()-timedelta(hours=24)).delete()
