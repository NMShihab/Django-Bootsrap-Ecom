from django.urls import path
from Login_App import views

app_name = "Login_App"

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    # path('login/', views.login_page, name='login'),
]
