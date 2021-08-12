from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import CreateUserAPIView, ObtainToken, UserUpdateAPIView
urlpatterns = [
    # path('token/', obtain_jwt_token),
    path('create/', CreateUserAPIView.as_view()),
    path('obtain_token/', ObtainToken.as_view()),
    path('update/', UserUpdateAPIView.as_view()),
]
