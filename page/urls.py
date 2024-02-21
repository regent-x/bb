from django.urls import path
from . import views 

app_name='page'

urlpatterns = [
    path('', views.home, name='home'),
    path('ceramic', views.ceramic, name='ceramic'),
    path('sculpture', views.sculpture, name='sculpture'),
    path('painting', views.painting, name='painting'),
    path('textile', views.textile, name='textile'),
    path('graphics', views.graphics, name='graphics'),
]