
from django.urls import path
from .views import home,RegisterView, LoginView, UserListView

urlpatterns = [

    path('', home, name='home'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/users/', UserListView.as_view(), name='user_list'),

]