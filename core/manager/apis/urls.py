from django.urls import path
from core.manager.apis import api

urlpatterns = [
    path('employees', api.employees_api_view, name='api_get_employees_view'),
    path('employee/<int:pk>', api.employee_detail_api_view, name='api_details_employee_view'),
    # path('test', api.test, name='test_api_view'),  # prueba de api
]
