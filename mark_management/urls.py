from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^', "mark_management.views.index"),
)
