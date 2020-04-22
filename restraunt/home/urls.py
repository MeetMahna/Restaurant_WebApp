from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('menu', views.menu, name="menu"),
    path('category/<int:id>/<int:qty>', views.category, name="category"),
    path('checkout', views.checkout, name="checkout"),
    path('delete_item/<int:id>', views.delete_item, name="delete_item"),
    path('clear_cart', views.clear_cart, name="clear_cart"),
    path('summary', views.summary, name="summary"),
]