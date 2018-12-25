# render 和 HttpResponse 两种方式
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 所有测试网页的入口
def index(request):
    return render(request, 'index.html')


# 第一个 view
def hello(request):
    return HttpResponse("Hello world ! ")


# 第二个 view
def ashida(request):
    context = {}
    context['ashida'] = 'Hello world from ashida!'
    return render(request, 'hello.html', context)

