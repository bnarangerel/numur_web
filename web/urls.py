from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='base'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('personal_line/', views.personal_line, name='personal_line'),
    path('leasing_line/', views.leasing_line, name='leasing_line'),
    path('student/', views.student, name='student'),
    path('women/', views.women, name='women'),
    path('auto/', views.auto, name='auto'),
    path('farmer/', views.farmer, name='farmer'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)