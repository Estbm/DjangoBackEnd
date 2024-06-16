from core.security.apis import api
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup', api.sign_up, name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test', api.test, name='test_security'),  # prueba de api
    path('test_token', api.test_token, name='test_token')  # prueba de token
]
