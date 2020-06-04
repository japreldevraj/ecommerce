from django.shortcuts import render

# Create your views here.
def aboutview(request):
    return render(request,'about.html')
def homeview(request):
    return render(request,'index.html')
def careview(request):
    return render(request,'care.html')
def holdview(request):
    return render(request,'hold.html')
def kitchenview(request):
    return render(request,'kitchen.html')
def codesview(request):
    return render(request,'codes.html')
def contactview(request):
    return render(request,'contact.html')
