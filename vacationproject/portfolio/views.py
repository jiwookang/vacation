from django.shortcuts import render
#모델에서 portfolio객체 가져오기
from .models import Portfolio
# Create your views here.
#def portfolio(request):
#    return render(request, 'portfolio/portfolio.html')

#기존 portfolio.html만 보여주었던 것을 modle과 연결해서 데이터를 받아오기
def portfolio(request):
    portfolio = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolio':portfolio})
