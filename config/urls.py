from django.contrib import admin
from django.urls import path, include
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/poll
    path('poll/', include('poll.urls')),
    # 127.0.0.1:8000/
    path("", views.index)
]
