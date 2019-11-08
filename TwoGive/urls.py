from django.urls import path

from TwoGive.views import customerProfileView, cartView, myItems, ProductDetail
from . import views

urlpatterns = [
    path('customerProfile/', customerProfileView.as_view(), name='customerprofile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('login/', views.LogIn.as_view(), name='login'),
    path('renterProfile/', views.renterProfileView.as_view(), name='renterprofile'),
    path('customerProfile/cart/', cartView.as_view(), name='cartview'),
    path('customerProfile/myItems', myItems.as_view(), name='myitemview'),
    path('customerProfile/items/<int:pk>', ProductDetail.as_view(), name='items_detail_view'),
    # path('customerProfile/items/add/<int:item_id>',views.add_to_cart, name='add_to_cart'),
    # path('logout/', views.logout_view, name='logout'),
]
