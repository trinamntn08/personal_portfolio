from django.shortcuts import render
from main.models import *
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, get_connection
from .forms import ContactForm
from personal_portfolio.settings import EMAIL_HOST_USER

# Create your views here.
class mainpage(SuccessMessageMixin, ListView,FormView):
    model = Project
    template_name = 'main.html'
    context_object_name = 'list_projects'  # name of the var in html template
    queryset = Project.objects.all().order_by("-pub_date")  # list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/'  # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.smtp.EmailBackend')
        send_mail(
            cd['name'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['trinamntn08@gmail.com'],
            fail_silently=False
        )
        return super(mainpage, self).form_valid(form)


def project_index(request):
    projects= Project.objects.all()
    context={
        'projects': projects
    }
    return render(request,'project_index.html',context)


def project_detail(request,pk):
    project= Project.objects.get(pk=pk)
    context={
        'project':project
    }
    return render(request,'project_detail.html',context)