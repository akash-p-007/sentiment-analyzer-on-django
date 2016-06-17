from django.shortcuts import render
def index(request):
    return render(request,'personal/home.html')
def contact(request):
    return render(request,'personal/basic.html',{'content':['if u waana contact then email','ama@gmail.com']})

