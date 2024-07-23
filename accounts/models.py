from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    
class Apiary(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Threshold(models.Model):
    hive_id = models.IntegerField()
    parameter = models.CharField(max_length=100)
    value = models.FloatField()

class Hive(models.Model):
    apiary = models.ForeignKey(Apiary, related_name='hives', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    weight = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} in {self.apiary.name}"


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MpesaResponseBody(AbstractBaseModel):
    body = models.JSONField()


class Transaction(AbstractBaseModel):
    phonenumber = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    receipt_no = models.CharField(max_length=100)

    def __str__(self):
        return self.receipt_no