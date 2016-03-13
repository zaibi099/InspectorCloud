from django.conf.urls import url, patterns
from InspectorCloud.views import home

urlpatterns = patterns('',

                       # url(r'^index',  IndexView.as_view()),
                       # url(r'^detail', DetailView.as_view()),
                       # url(r'^result', ResultsView.as_view()),
                       # Examples:
                       url(r'^index/$', 'InspectorCloud.views.home', name='home'),
                       url(r'^generateKey/$', 'InspectorCloud.views.instance', name='instance'),
                       url(r'^Layout/$', 'InspectorCloud.views.Layout', name='Layout'),
                       url(r'^alarms/$', 'InspectorCloud.views.alarms', name='alarms'),
                       url(r'^resourcemonitoring/$', 'InspectorCloud.views.resourcemonitoring',name='resourcemonitoring'),
                       url(r'^instance/$', 'InspectorCloud.views.instance', name='instance'),
                       url(r'^debugging/$', 'InspectorCloud.views.debugging', name='debugging'),
                       url(r'^error/$', 'InspectorCloud.views.error', name='error'),
                       url(r'^warning/$', 'InspectorCloud.views.warning', name='warning'),
                       url(r'^event/$', 'InspectorCloud.views.event', name='event'),
                       url(r'^resourceusage/$', 'InspectorCloud.views.resourceUsage', name='resourceUsage'),

                       )
