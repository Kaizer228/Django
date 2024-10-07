
from django.urls import include, re_path
import app.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^', app.views.dashboard, name='dashboard')
]
