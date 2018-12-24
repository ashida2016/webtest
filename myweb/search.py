# render 和 HttpResponse 两种方式
from django.shortcuts import render
from django.http import HttpResponse


# 表单
def search_form(request):
    return render(request, 'dbtest.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

