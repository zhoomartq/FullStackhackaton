from django.urls import path

from . import views
from .views import ForgotPassword, ForgotPasswordComplete

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view(), name='activation_code'),
<<<<<<< HEAD
]
=======
    path('forgot_password/', ForgotPassword.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplete.as_view()),
]

>>>>>>> 9d90a02bab683a1ae2a7b952301031832d4bae77
