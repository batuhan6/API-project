from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('users/', include('djoser.urls')),
    path('manager/', include('users.urls_manager')),
    path('delivery-crew/', include('users.urls_delivery_crew'))
]
