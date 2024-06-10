from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_page, name='login'),
    path('register/', views.registration, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('company-register/', views.company_register, name='company_register'),
    path('company-register/add-code/', views.add_code, name='add_code'), 
    path('company-register/add-company/', views.add_company, name='add_company'),
    path('company-edit/', views.company_edit_view, name='company_edit' ),
    path('branch/', views.branch_list_view, name='branch'),
    path('branch/edit/<int:pk>/', views.branch_edit_view, name='branch_edit'),
    path('branch/<int:pk>/users/', views.branch_view_users, name='branch_users'),
    
]