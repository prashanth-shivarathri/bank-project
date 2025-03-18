from django.db import models

# Create your models here.
class gender(models.Model):
     gender=models.CharField(max_length=7)

     def __str__(self):
          return self.gender

class Bank(models.Model):
     name=models.CharField(max_length=32)
     account=models.BigIntegerField(unique=True)
     email=models.EmailField()
     aadhar=models.CharField(max_length=12)
     dob=models.DateField()
     photo=models.ImageField(upload_to='images')
     balance=models.DecimalField(default=500,decimal_places=2,max_digits=10)
     pin=models.IntegerField(default=0)
     phone=models.BigIntegerField()
     gender=models.ForeignKey(gender,on_delete=models.CASCADE)