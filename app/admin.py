from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(UserProfile) #we have only one table , UserProfileManager is not a table it is for managing the Userprofile