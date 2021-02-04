from django.urls import path
from accounts.views import (
    signup_view,
    login_view,
    logout_view
)


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name="sign_up"),
    path('login/', login_view, name="log_in"),
    path('logout/', logout_view, name="log_out"),
]