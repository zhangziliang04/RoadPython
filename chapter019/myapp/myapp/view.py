# 视图
from django.http import HttpResponse
from django.shortcuts import render


# 无模板的情况：控制器和内容耦合
def hello1(request):
    return HttpResponse("Hello world ! ")


# 调用模板的情况：控制器和内容解耦
def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)