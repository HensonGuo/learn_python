#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from learn.models import Person, CustomFieldTest

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse('Hello World!')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def test(request):
    string = u"我在学习Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'test.html', {'string': string, 'TutorialList':TutorialList, 'info_dict':info_dict, 'List':List})


def test_render_2_response(request):
    return render_to_response('home.html')


def model_test(request):
    nme = request.GET['name']
    age = request.GET['age']
    p = Person.objects.filter(name = nme)
    if not p:
        Person.objects.create(name = nme, age = age)
    else:
        person = p[0]
        nme = person.name + '- get from db'
        age = '{}- get from db'.format(person.age)
    return render(request, 'test_model.html', {'name':nme, 'age':age})

def field_test(request):
    p = CustomFieldTest.objects.get_or_create(name='abc', labels = ["Python", "Django"])
    return render(request, 'test_fields.html')