from django.urls import path
from vuelos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.vuelos, name="Vuelos"),
    
]
