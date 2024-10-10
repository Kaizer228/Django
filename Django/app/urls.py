
 
from django.urls import path
import app.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    path(r'', app.views.dashboard, name='dashboard'),
    path(r'edit/', app.views.edit, name='edit'),
]
