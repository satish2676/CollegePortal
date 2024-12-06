from django.urls import path
from . import views

urlpatterns =[
    path('', views.admin_login, name='admin_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('base/',views.base, name='base'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('edit-student/<str:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<str:student_id>/', views.delete_student, name='delete_student'),
  
    path('home/',views.home, name='home'),
    path('marks/',views.marks, name='marks'),
    path('attendance/',views.attendance, name='attendance'),
    path('backlogs/',views.backlogs, name='backlogs'),
    path('personal_details/',views.personal_details, name='personal_details'),
    path('fee_details/',views.fee_details, name='fee_details'),
    path('complaints/',views.complaints, name='complaints'),
    path('logout/',views.logout, name='logout'),
]