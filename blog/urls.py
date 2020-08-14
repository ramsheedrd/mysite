from . import views as v
from django.urls import path

urlpatterns = [
    path('', v.PostList.as_view(), name='home'),
    path('<slug:slug>/', v.PostDetail.as_view(), name='post_detail'),
    path('register/', v.register, name='register'),
    path('login/', v.login, name='login'),
    path('logout/', v.logout, name='logout'),
]
