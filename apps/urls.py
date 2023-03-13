from django.urls import path

from apps.views import index_page, menu_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('menu', menu_page, name='menu_page'),
]
