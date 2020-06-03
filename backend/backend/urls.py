from django.urls import path, include  # add this
from rest_framework import routers  # add this
from django.conf.urls import url, include
from django.contrib import admin


app_name = "reward"
router = routers.DefaultRouter()  # add this



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('reward.urls')),  # add this


]


# https://www.tutorialspoint.com/django/django_url_mapping.htm
