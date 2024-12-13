
from django.urls import path
from .views_api import RegisterView, LoginView, UserListView,VerifyUserView,UpdateUserView,DeleteUserView
from users import views

urlpatterns = [

    
    #API END POINTS URLS
    path('api/verify-user/<int:user_id>/', VerifyUserView.as_view(), name='verify-user'),
    path('api/register/', RegisterView.as_view(), name='register_api'),
    path('api/login/', LoginView.as_view(), name='login_api'),
    path('api/users/', UserListView.as_view(), name='userlist_api'),
   
    path('users/<int:user_id>/', UpdateUserView.as_view(), name='update-user'),  # Update user data
    path('users/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete-user'),  # Delete a user


    #FRONT END URLS:
    #ADMIN DASHBOARD
    path('signup/', views.signup_page, name='signup'),
    path('add-user/', views.add_user, name='add_user'),

    #ADMIN DASHBOARD 
    path('login/', views.LoginPage, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),   
    path('Logout/', views.LogoutPage, name='logout'),

    #USER DAHSBOARD
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
   

]