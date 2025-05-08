from django.urls import path
from . views import home, delete_prof
urlpatterns = [
   path('', home, name='home'),
   path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
]