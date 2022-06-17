from django.contrib import admin
from .models import Cities, Profile

admin.site.register([Cities, Profile])