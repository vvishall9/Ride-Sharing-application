from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('carsearch', views.carsearch, name='carsearch'),
    path('info', views.info, name='info'),
    path('signup',views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
