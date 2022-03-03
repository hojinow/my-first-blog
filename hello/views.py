from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello/Index',
            'msg': 'Could you please fill in your info?',
            'form': HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'Your name is: ' + request.POST['name']+ \
            ' and your email is: ' + request.POST['mail'] + ' . Also your age is: ' \
            + request.POST['age']
        self.params['msg'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
