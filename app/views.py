from django.shortcuts import render

# Create your views here.
def happy(request):
    return render(request,'happy.html')


def sad(request):
    return render(request,'sad.html')