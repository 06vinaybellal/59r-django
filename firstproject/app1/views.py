from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def view1(request):
    return HttpResponse("i am view1")
def view2(request):
    return HttpResponse("i am view2")
def view3(request):
    return JsonResponse({"name":"abc","age":22})
def dynamicview4(request):
    qp1=request.GET.get("name")
    return HttpResponse(f"hello {qp1}")

def view5(request):
    name=request.GET.get("name","aaa")
    age=request.GET.get("age",22)
    info={"name":name}

def temp1(request):
    return render (request,"./simple.html")
def temp2(request):
    return render (request,"./second.html")

