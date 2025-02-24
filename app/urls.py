from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index2/', views.index2),
    path('index3/', views.index3),
    path('index4/', views.index4),
    path('index5/', views.index5),
    path('char/', views.char),
    path('digit/<int:dig>/', views.digit_check),
    path('control/', views.control),
    path('dict/', views.dict),
    path('empdetails/', views.empviews),
    path('product/', views.productview),
    path('user/', views.userview),
    path('load/', views.loadview),
    path('products/<int:id>/', views.product_view),

]