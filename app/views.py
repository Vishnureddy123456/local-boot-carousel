from django.shortcuts import render

# Create your views here.
def local_boot(request):
    return render(request,'local_boot.html')
