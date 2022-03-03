from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import JisroundingForm
from decimal import Decimal

class Jisview(TemplateView):

    def __init__ (self):
        self.params = {
            'title': 'JIS Rounding of Numbers',
            'top_message': 'Comming soon !!!',
            'form': JisroundingForm(),
            'bottom_message': ""
        }

    def get (self, request):
        self.params = {
            'title': 'JIS Rounding of Numbers',
            'top_message': 'Please fill in the measured value and digit of the value you want to get &#129315;',
            'form': JisroundingForm(),
            'bottom_message': "&#129315;"
        }
        return render (request, 'jisrounding/main.html', self.params)

    def post (self, request):
        #calculation
        v = Decimal(str(request.POST['value'])) #Not sure whether Decimal is needed  to DecimalField
        d = int(request.POST['digit'])
        try:
            answer = str(round(v,d))
        except:
            answer = None #if digit is too large, the execution stops so put except

        self.params = {
            'title': 'JIS Rounding of Numbers',
            'top_message': "Rounded value is : " + str(answer),
            'form': JisroundingForm(request.POST),
            'bottom_message': "&#129315;"
        }
        return render (request, 'jisrounding/main.html', self.params)

#これからのアクション
#1 JIS丸めをpythonでできるようにプログルラム化(Jupyterで作る)
#2 プログラムをDeploy
#3 各回ごとにどの切り捨て方法を採ったか、コメントが下部に表示できるようにする
