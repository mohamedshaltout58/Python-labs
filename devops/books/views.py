from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def books(request):
    b1 = {"id":1, "name":"book1", "description":"book1_description"}
    b2 = {"id":2, "name":"book2", "description":"book2_description"}
    b3 = {"id":3, "name":"book3", "description":"book3_description"}
    bookinfo = [b1 , b2 , b3]
    return render(request,"landingpage.html",context={"b1":b1,"b2":b2,"b3":b3,"std":bookinfo})

def contactus(request):
    website = "www.iti.com"
    mobile = "01001234567"
    addr = "Elmansoura st."
    return render(request,"contactus.html",
                  context={"mob":mobile,"web":website,"address":addr})

def aboutus(request):
    return render(request,"aboutus.html")