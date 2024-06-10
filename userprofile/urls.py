from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account-config/', views.account_config, name='config'),
    path('deactivate/', views.account, name='deactivate'), 
]