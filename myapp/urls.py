from django.conf.urls import url, include

from . import views

app_name = "myapp"

urlpatterns = [
    url(r'^$',  views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$',  views.SchoolDetailView.as_view(), name='list'),
]
