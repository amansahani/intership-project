from django.shortcuts import render

from students.forms import StudentForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            # Redirect to a success page or perform any other action
    else:
        form = StudentForm()
    return render(request, 'students/index.html', {'form': form})