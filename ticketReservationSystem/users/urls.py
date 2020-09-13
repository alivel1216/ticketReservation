from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.registro, name="Registro"),        
    path('login',views.loginPage, name="Login"),        
    path('logout',views.loginPage, name="Logout"),        
]