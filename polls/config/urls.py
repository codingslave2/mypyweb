from django.contrib import admin
from django.urls import path

from  import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),
    path('', views.index),
]
