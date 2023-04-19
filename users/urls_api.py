from django.urls import path, include
from users import views_api

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('users/', include('djoser.urls')),
    path('manager/', include('users.urls_group')),
    path('delivery-crew/', include())
]
