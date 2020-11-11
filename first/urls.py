from django.urls import path, include


from first import views

from .views import ShopCreate, ShopUpdate, ShopDelete, ShopList, ShopDetail

urlpatterns = [

    path('',views.home, name = 'home'),
    path('create',ShopCreate.as_view(), name = 'create'),

    path('update/<pk>',ShopUpdate.as_view(), name = 'update'),

    path('delete/<pk>',ShopDelete.as_view(), name = 'delete'),

    path('list',ShopList.as_view(),name = 'list'),


    path('detail/<pk>',ShopDetail.as_view(), name = 'detail'),

]
