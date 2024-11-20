from django.urls import path
from . import views

urlpatterns = [
    path('hospitals', views.HospitalViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('hospital_user', views.HospitalUserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))

]