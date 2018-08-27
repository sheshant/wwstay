from django.conf.urls import url, include
from django.views.generic import TemplateView

from expenses import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^expenses/$', views.expense_list, name='expense_list'),
    url(r'^expenses/create/$', views.expense_create, name='expense_create'),
    url(r'^expenses/(?P<pk>\d+)/update/$', views.expense_update, name='expense_update'),
    url(r'^expenses/(?P<pk>\d+)/delete/$', views.expense_delete, name='expense_delete'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),

]
