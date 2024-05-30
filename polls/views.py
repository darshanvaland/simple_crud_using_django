from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import crate
from .forms  import createform 


# Create your views here.

def index(request):
    data = {}
    data['dataset'] = crate.objects.all()
    # print(data) 
    return render(request ,"index.html" , data)
def hello(request):
    return HttpResponse("hiiii")
def darshan(request):
    return HttpResponse("hiiiiiiiiiiiiiiiiii")
def create(request):
    form = createform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request , "create.html")
def edit(request, id):
    data = {}
    data['dataset'] = crate.objects.get(id=id)
    form = createform(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"edit.html",data)
def update(request,id):
    data= crate.objects.get(id=id)  
    form = createform(request.POST, instance = data)  
    if form.is_valid():  
        form.save()  
        return redirect("index")  
    return render(request,"edit.html",data)
def delete(request,id):
    data = crate.objects.get(id=id)
    data.delete()
    return  redirect('index')