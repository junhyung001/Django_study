from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def calculator(reqeust):
    # return HttpRequest('계산기 구현 기능 시작입니다.')
    return render(reqeust, 'calculator.html')