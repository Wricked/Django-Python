from django.conf.urls import patterns, url

from employees import views


#Url patterns, showing according ids.
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^employees/(?P<employee_id>\d+)$', views.show, name='show'),
    url(r'^employees/list$', views.list, name='list'),
    url(r'^employees/new_employee$', views.new_employee, name='new_employee'),
    url(r'^employees/delete_employee$', views.delete_employee, name='delete_employee'),
    url(r'^employees/new_department$', views.new_department, name='new_department'),

)