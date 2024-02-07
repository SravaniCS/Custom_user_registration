from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserProfileManager(BaseUserManager):
    #it consists of 2 methods create_user,create_superuser
    def create_user(self,email,first_name,last_name,password=None):
        #mail is mandatory field if it is not provided raise a valueError
        if not email:
            raise ValueError('Please Provide a Email')

        #if email is available then normalize_email(method of baseusermanager)
        ne=self.normalize_email(email)
        #create an object for the UserProfile
        upo=self.model(email=ne,first_name=first_name,last_name=last_name)
        #Encrypt the password
        upo.set_password(password)
        upo.save()
        #return the object becoz we need to use the same in the create_superuser
        return upo

    def create_superuser(self,email,first_name,last_name,password):
        #used all the properties of create_user and made is_staff and superuser to true
        upo=self.create_user(email,first_name,last_name,password)
        upo.is_staff=True
        upo.is_superuser=True
        upo.save()


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True) #is active is true for both normal user and superuser
    is_staff=models.BooleanField(default=False) #this is true for superuser and false for normal user so we'll make it false and change in create_superuser
    is_superuser=models.BooleanField(default=False) #same as staff
    #objects is used to connect the UserProfile to UserProfileManager
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']