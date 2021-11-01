from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin



#-----USER CREATION MANAGER---------
class CustomUserManager(BaseUserManager):
    def create_user(self, email , FirstName, LastName, password):
        user = self.model(email= email, FirstName=FirstName, LastName=LastName, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using= self.db)
        return user

    def create_superuser(self, email , FirstName, LastName, password):
        user=self.create_user(email, FirstName, LastName, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self.db)
        return user
    
    def get_by_natural_key(self, email_):
        return self.get(email = email_)


#-----USER MODEL---------
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200 , verbose_name = 'почта', unique=True)
    FirstName = models.CharField(max_length= 200, verbose_name = 'Имя',)
    LastName = models.CharField(max_length= 200, verbose_name = 'фамилия')
    Address = models.CharField(max_length= 200, verbose_name = 'Адрес')
    PhoneNumber = models.DecimalField(max_digits = 25, verbose_name = 'Номер телефона', decimal_places = 20, null= True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['FirstName', 'LastName', 'password']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def natural_key(self):
        return self.email