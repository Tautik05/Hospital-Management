from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.DoctorViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('department', views.DepartmentViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('specialization', views.SpecilizationViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))

]