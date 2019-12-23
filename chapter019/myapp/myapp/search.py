# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from . import dbhandler


# 表单
def login_form(request):
    return render(request, 'name.html')


# 接收请求数据
def login(request):
    request.encoding = 'utf-8'
    if 'Name' in request.GET and request.GET['Name']:
        message = '姓名: ' + request.GET['Name'] + '电话：' + request.GET['Tel']
        # 数据模型调用
        dbhandler.add_name(request.GET['Name'])
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

