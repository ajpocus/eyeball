from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tasks.views',
    url(r'^$', 'tasks_list'),
#    url(r'^finished/$', 'tasks_list_finished'),
    url(r'^add/', 'tasks_add'),
#    url(r'^(?P<task_id>\d+)', 'tasks_start'),
)
    
