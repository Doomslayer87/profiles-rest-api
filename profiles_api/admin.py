from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)  
"""questo dice a django di utilizzare il nostro UserProfile model definito in precedenza in models.py e lo rende accessibile all'interfaccia
    "admin site"
"""


# Register your models here.
