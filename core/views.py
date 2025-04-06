from django.shortcuts import render
from newapp.tasks import calculate_sum


def home(request):
    context = {
        "message": "Welcome to My Django App! vdfdfd"
    }
    return render(request, "index.html", context)

def task_page(request):
    calculate_sum.delay(2, 3)
    return render(request, "task.html")
