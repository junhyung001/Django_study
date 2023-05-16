from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def calculator(reqeust):
    # 1 데이터 확인
    num1 = reqeust.GET.get('num1')
    num2 = reqeust.GET.get('num2')
    opearators = reqeust.GET.get('opearators')
    
    # 2 데이터 연산
    if opearators == '+':
        result = int(num1) + int(num2)
    elif opearators == '-':
        result = int(num1) - int(num2)
    elif opearators == '*':
        result = int(num1) * int(num2)
    elif opearators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    # 결과값 보냄
    return render(reqeust, 'calculator.html', {'result' : result})