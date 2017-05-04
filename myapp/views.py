from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from . import models

# Create your views here.


# GenericCBVs
class SchoolListView(ListView):
    context_object_name = 'schools' # Default would be 'school_list'
    model = models.School
#    template_name = 'myapp/school_list.html' # Default name


class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = models.School
#    template_name = 'myapp/school_detail.html' # Default name


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
#    template_name = 'myapp/school_form.html' # Default name


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School
#    template_name = 'myapp/school_form.html' # Default name


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('myapp:list')
#    template_name = 'myapp/school_confirm_delete.html' # Default name
