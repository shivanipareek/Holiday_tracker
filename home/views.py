from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render


class Homeview(TemplateView):
    template_name = 'home/home.html'

    def profile(request):
        import pdb
        pdb.set_trace()
        args = {'user': request.user}
        return render(request,'home/home.html',args)