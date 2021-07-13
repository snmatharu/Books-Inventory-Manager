from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import Addbooks

def AddData(request):
    
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('author') :
            post=Addbooks()
            
            post.title= request.POST.get('title')
            post.author= request.POST.get('author')
            post.genre= request.POST.get('genre')
            post.language= request.POST.get('language')
            post.save()

            
            return render(request, 'create.html')  
    else:
        return render(request,'create.html')

def GetData(request):

    data = Addbooks.objects.all()
    datagenre = Addbooks.objects.values('genre').distinct()
    datalanguage = Addbooks.objects.values('language').distinct()
    filtergenre = request.GET.get('genre')
    filterlanguage = request.GET.get('language')
    
    if(filtergenre):
        data = Addbooks.objects.all().filter(genre= filtergenre)
    elif(filterlanguage):    
        data = Addbooks.objects.all().filter(language= filterlanguage)
    else:
        data = Addbooks.objects.all()

    return render(request,"show.html", {"books_data": data, "discgenre": datagenre, "disclanguage":datalanguage})