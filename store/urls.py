from django.urls import path
from .views import Login, Signup, Index, Logout, Cart, OrdersView, CheckOut
from .middleware import check_authorization

urlpatterns=[
    path('',Index.as_view(),name="index"),
    path('signup/',Signup.as_view(),name="signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout"),
    path('cart/',Cart.as_view(),name="cart"),
    path('orders/',check_authorization(OrdersView.as_view()),name="order"),
    path('checkout/',check_authorization(CheckOut.as_view()),name="checkout"),     
]