from django.db import models
from django.core.validators import RegexValidator  

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Name')
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Email')
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True, verbose_name='Photo', max_length=100)
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name='Place')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number', validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
        ),
    ])

    def __str__(self):
        return self.name
