from django.conf.urls import url, patterns
from InspectorCloud.views import index

urlpatterns = patterns('',
                        url(r'^index/$', 'InspectorCloud.views.index', name='index'),
                        url(r'^createAlarm/$', 'InspectorCloud.views.createAlarm', name='createAlarm'),
                        url(r'^alarmList/$', 'InspectorCloud.views.alarmList', name='alarmList'),
                        url(r'^createBill/$', 'InspectorCloud.views.createBill', name='createBill'),
                        url(r'^generateBill/$', 'InspectorCloud.views.generateBill', name='generateBill'),
                        url(r'^invoice/$', 'InspectorCloud.views.invoice', name='invoice'),
                        url(r'^createInstance/$', 'InspectorCloud.views.createInstance', name='createInstance'),
                        url(r'^createRouter/$', 'InspectorCloud.views.createRouter', name='createRouter'),
                        url(r'^loginForm/$', 'InspectorCloud.views.loginForm', name='loginForm'),
                        url(r'^registerUser/$', 'InspectorCloud.views.registerUser', name='registerUser'),

                        url(r'^resourceQuotas/$', 'InspectorCloud.views.resourcesQuotas', name='resourceQuotas'),
                        url(r'^runningVms/$', 'InspectorCloud.views.runningVms', name='runningVms'),
                        url(r'^happenings/$', 'InspectorCloud.views.happenings', name='happenings'),
                        url(r'^stats/$', 'InspectorCloud.views.stats', name='stats'),

                        url(r'^warnings/$', 'InspectorCloud.views.warnings', name='warnings'),
                        url(r'^errors/$', 'InspectorCloud.views.errors', name='errors'),
                      )