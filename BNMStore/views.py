from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from service.models import service
from news.models import news
from contactenquiry.models import contactenquiry
from django.core.paginator import Paginator


def home(request):
    newsData=news.objects.all()
    serviceData=service.objects.all()
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            serviceData=service.objects.filter(service_title__icontains=st)
    data={
        'serviceData':serviceData,
        'newsData':newsData
    }
    return render (request, 'index.html',data)


def newsdetails(request,slug):
    newsdetails=news.objects.get(new_slug=slug)
    data={
        'newsdetails':newsdetails
    }
    return render (request, 'newsdetails.html',data)


def aboutus(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render (request, 'about.html',{'output':output})


def services(request):
    serviceData=service.objects.all()
    paginator = Paginator(serviceData,2)
    pagenumber= request.GET.get('page')
    servicedatafinal=paginator.get_page(pagenumber)
    totalpage = servicedatafinal.paginator.num_pages
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            serviceData=service.objects.filter(service_title__icontains=st)
    data={
        'serviceData':servicedatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render (request, 'services.html',data)


def userform(request):
    finalans=0
    data={}
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render (request, 'userform.html',{'error':True})
            # n1=int(request.GET.get['num1'])
            # n2=int(request.GET.get['num2'])
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        print(n1+n2)
        finalans=n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
            }
               # url="/about-us/?output={}".format(finalans)
                # return HttpResponseRedirect(url)
    return render (request, 'userform.html',data)

    # fn=usersform()
    # data={'form':fn}
    # try:
    #     if request.method=="POST":
    #     # n1=int(request.GET.get['num1'])
    #     # n2=int(request.GET.get['num2'])
    #         n1=int(request.POST.get('num1'))
    #         n2=int(request.POST.get('num2'))
    #         print(n1+n2)
    #         finalans=n1+n2
    #         data={
    #             'form':fn,
    #             'output':finalans
    #         }
    #         # url="/about-us/?output={}".format(finalans)
    #         # return HttpResponseRedirect(url)
    # except:
    #     pass

# def serviceDT(request):
#     serviceData=service.objects.all()



def contactus(request):
    return render (request, 'contact.html')

def saveenquiry(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        messege= request.POST.get('messege')
        narin=contactenquiry(contact_name=name,contact_email=email,contact_phone=phone,contact_messege=messege)
        narin.save()
    return render (request, 'contact.html')








# () != @