from django.conf.urls import url, include

from . import views

app_name = "myapp"

urlpatterns = [
    url(r'^$',                 views.SchoolListView.as_view(),   name='list'),
    url(r'^(?P<pk>\d+)/$',     views.SchoolDetailView.as_view(), name='detail'),
    url(r'^new/$',             views.SchoolCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/upd/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/del/$', views.SchoolDeleteView.as_view(), name='delete'),
]
