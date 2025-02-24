from django.urls import path
from .views import recipes_view, recipe_detail_view

urlpatterns = [
    path('recipes/', recipes_view, name='recipes_view'),
    path('recip_details/<int:recipe_id>/', recipe_detail_view, name='recipe_detail_view'),
]
