from django.db import models

# Create your models here.

class PayPlan (models.Model):
    name = models.CharField (max_length=20)
    price = models. IntegerField()
    updated_at = models. DateTimeField (auto_now=True)
    create_at = models.DateTimeField (auto_now_add=True)


from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User as U
# Create your models here.
class Users (AbstractUser):
    pay_plan = models. ForeignKey (PayPlan, on_delete=models.DO_NOTHING)


class UserDetail (models.Model):
    user = models. OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models. ForeignKey (PayPlan, on_delete=models.DO_NOTHING)