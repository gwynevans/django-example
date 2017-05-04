from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView

from . import models

# Create your views here.


# GenericCBVs
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'myap-/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = models.School
    template_name = 'myapp/school_detail.html'
