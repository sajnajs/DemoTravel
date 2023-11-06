from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team


def demo(request):
    obj = place.objects.all()

    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})


















# def fun1(request):
#     return render(request,"contact.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})



# Create your views here.
# def home(request):
#     return HttpResponse("Hiii Iam Home.....")

# def contact(request):
#     return HttpResponse("Contact details")
#
# def details(request):
#     return render(request,'details.html')
#
# def thanks(request):
#     return HttpResponse("Thank You")
