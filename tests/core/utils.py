from django.test import RequestFactory
from django.contrib.auth.models import User
from apps.usuarios.api.views import LoginView

user = User(
            username="TestUser",
            email="Test@test.com",
            first_name="Test",
            last_name="User",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

user_data = {
    'username': user.username,
    'email': user.email,
    'password': 'T3st1ng.',
    'first_name': user.first_name,
    'last_name': user.last_name,
    'is_superuser': user.is_superuser,
    'is_staff': user.is_staff,
    'is_active': user.is_active
}

login_data = {
    'username': user.username,
    'password': 'T3st1ng.'
}

def get_auth_token(data):
    view = LoginView.as_view()
    token = view(RequestFactory().post('/api/v1/user/login', data=data))
    return token.data['access']