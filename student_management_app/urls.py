from django.urls import path
from . views import home, delete_prof, create_prof, update_prof
urlpatterns = [
   path('', home, name='home'),
   path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
   path('create_page/', create_prof, name='create_prof'),
   path('update_prof/<int:id>/', update_prof, name='update_prof'),
]