from django.urls import path
from .views import portfolio_view,download_file

urlpatterns = [
    path('portfolio/', portfolio_view,name='portfolio'),
    path('portfolio/download_file(<str:name>)', download_file,name='download_file'),
]