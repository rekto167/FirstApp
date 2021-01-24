from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    IndexChefView,
    MenuList,
    AddMenu,
)

app_name = 'chef'
urlpatterns = [
    path('addmenu/', AddMenu.as_view(), name='addmenu'),
    path('listmakanan/', MenuList.as_view(), name='listmakanan'),
    path('', IndexChefView.as_view(), name='index'),
]
