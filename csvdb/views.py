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
        messages.success(request, "file uploaded")
        return render(request,'csvdb/index.html')