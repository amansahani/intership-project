import os
from django.shortcuts import render
from django.contrib import messages

from csvdb.models import CSVDB
from csvdb.visualization import visualize



# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'csvdb/index.html')
    elif request.method == 'POST':
        file = request.FILES["file"]
        obj = CSVDB.objects.create(file=file)
        visualize(obj.file)
        filename = obj.file.name[6:]
        img_pie = f"{filename}-pie.png"
        img_bar = f"{filename}-bar.png"
        context = {"bar": img_bar, "pie":img_pie }
        messages.success(request, "file uploaded")
        return render(request,'csvdb/result.html',context)