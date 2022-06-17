from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from myapp.models import student

def sayhello(request):
    return HttpResponse('sayhello....')

def hello2(request, username):
    now = datetime.now()
    return render(request, 'hello3.html', locals())

def hello4(request, username):
    now = datetime.now()
    return render(request, 'hello4.html', locals())
    
def test_dict(request):
    dict1 = {'key1': 123, 'key2': 456}
    return render(request, 'hello4.html', dict1)
    
def dice(request):
    no = random.randint(1,6)
    return render(request, 'dice.html', {"no":no})
    
def dice2(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    return render(request, 'dice2.html', locals())
    
times=0
def dice3(request):
    global times      # 宣告 global 變數
    times = times + 1
    local_times=times # 指派給 區域變數 local_times
    username="David"
    dict_no={"no":random.randint(1,6)}   # 1~6   
    return render(request,"dice3.html",locals())
   
def show(request):
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    list1 = []
    for i in range(1,10):
        for j in range(1,10):
            k = i * j
            list1.append([i, j, k])
    return render(request,"show.html",locals())
    
def listone(request):
    try:
        unit = student.objects.get(cName='chris')
        print('student.objects.get', type(unit))
    except:
        errormessage = "(讀取錯誤!"
    return render(request,"listone.html",locals())
    
def listall(request):
    students = student.objects.all().order_by('id')
    print('student.objects.all()', type(students))
    return render(request,"listall.html",locals())

def listdata(request):
    students = student.objects.all().order_by('id')
    print('student.objects.all()', type(students))
    return render(request,"listdata.html",locals())