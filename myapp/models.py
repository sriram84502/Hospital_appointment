from django.db import models
from django.contrib.auth.models import AbstractUser,User
import uuid
from django.core.validators import RegexValidator

# Create your models here.
phone_validator = RegexValidator(r"^[0-9]{10}$", "The phone number provided is invalid")

class Patient(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,validators=[phone_validator],unique=True)
    is_phone_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=16,unique=True)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    age = models.IntegerField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Doctors(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img')
    place=models.CharField(max_length=50)
    speciality_in=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    hospital=models.CharField(max_length=1000)
    hospitaladd=models.CharField(max_length=1000)
    class Meta:
        ordering = ('-place',)

class Transaction(models.Model):
    user=models.OneToOneField(Patient,on_delete=models.CASCADE,related_name="profile")
    phone1=models.CharField(max_length=10)
    #aadhar1=models.CharField(max_length=12)
    user1=models.CharField(max_length=100)
    otp=models.CharField(max_length=100,null=True,blank=True)
    day=models.CharField(max_length=50)
    slot=models.AutoField(primary_key=True)
    uid=models.UUIDField(default=uuid.uuid4)
    transaction_id=models.CharField(max_length=100,unique=True)

class Medications(models.Model):
    problem = models.CharField(max_length=100)
    medicine1 = models.CharField(max_length=100)
    medicine2 = models.CharField(max_length=100)
    medicine3 = models.CharField(max_length=100)
    advice = models.CharField(max_length=1000)