from django.conf.urls import url
from loan_app import views

app_name = 'loan_app'

urlpatterns = [
    url(r'^loan_list/', views.loan_list, name='list'),
    url(r'^create_loan/', views.create_loan, name='create'),
    url(r'^return_action/(?P<pk>\d+)/$', views.return_action, name='return_action'),
    url(r'^loan_detail/(?P<pk>\d+)/$', views.loan_detail, name='detail'),
    url(r'^user_login/', views.user_login, name='login'),
    url(r'^user_logout/', views.user_logout, name='logout'),
]
