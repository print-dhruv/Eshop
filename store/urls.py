from django.urls import path
from .views import Login, Signup, Index, Logout, Cart


urlpatterns=[
    path('',Index.as_view(),name="index"),
    path('signup/',Signup.as_view(),name="signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout"),
    path('cart/',Cart.as_view(),name="cart"),     
]