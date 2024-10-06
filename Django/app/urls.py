
from django.urls import include, re_path
import app.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^$', app.views.login, name='login'),
    re_path(r'^register$', app.views.register, name='register'),
    re_path(r'^dashboard', app.views.dashboard, name='dashboard')
]
