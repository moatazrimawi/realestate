from django.urls import path
from realestateapp import views
urlpatterns = [
    path('moataz',views.return_name),
    path('ola',views.return_name_ola_page)
]
