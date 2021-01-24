from django.shortcuts import render, redirect
from .models import Project,Product,Category
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import Contactform
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
import requests


def index(request):
    template = 'pages/index.html'
    product = Product.objects.all()
    projects = Project.objects.all()
    context = {'product':product, 'projectlist':projects}
    return render(request, template , context)

def about(request):
    template = 'pages/about_us.html'
    context = {}
    return render(request, template , context)

def projectdetail(request, project_slug):
    projectdetail = Project.objects.get(slug=project_slug)
    template = 'pages/project_detail.html'
    context ={'pd':projectdetail}
    return render(request, template , context)

def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    template = 'pages/product_detail.html'
    context ={'pd':productdetail}
    return render(request, template , context)    


def services(request):
    template = 'pages/services.html'
    context = {}
    return render(request, template , context)


def projects(request):
    template = 'pages/projects.html'
    category = Category.objects.all()
    projects = Project.objects.all()
    context = {'category':category,'projectlist':projects}
    return render(request, template , context)


def shop(request):
    product = Product.objects.all()
    template = 'pages/shop.html'
    context = {'product':product}
    return render(request, template , context)    


def contact(request):
    if request.method == 'GET':
        form = Contactform()
    else:
        form = Contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']
            msg_plain = render_to_string('email.txt', {'name': name ,'email': email,'category': category,'message':message})
            print(msg_plain)
            try:
                send_mail('This is a Test ',msg_plain,settings.EMAIL_HOST_USER,[settings.EMAIL_TARGET_RECIEVE],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home:success')
    context={'form':form}
    template = 'pages/contact.html'
    return render(request, template , context) 


def successView(request):
    return render(request,'pages/success.html')


def test(request):
    url = "https://en.wikipedia.org"
    apiKey = "qY3mfrk4agXooY3JMfn8JI7EhdKExPxBIB1aAErkWTx9GeLNJk5jlBkzvKHPUeGr"
    linkRequests = "https://api.html2pdf.app/v1/generate?url={0}&apiKey={1}".format(url, apiKey)
    request = requests.get(linkRequests).content
    context = {'product':product}
    return render(request,'pages/test.html',context)

# def Invoice_form(request):
#     if request.method == 'GET':
#         form = Contactform()
#     else:
#         form = Contactform(request.POST)
#         if form.is_valid():
#             Date = form.cleaned_data['date']
#             email = form.cleaned_data['email']
#             Address = form.cleaned_data['category']
#             Invoice Number = form.cleaned_data['message']
#             msg_plain = render_to_string('email.txt', {'name': name ,'email': email,'category': category,'message':message})
#             print(msg_plain)
#             try:
#                 send_mail('This is a Test ',msg_plain,settings.EMAIL_HOST_USER,[settings.EMAIL_TARGET_RECIEVE],fail_silently=False)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('home:success')
#     context={'form':form}
#     template = 'pages/contact.html'
#     return render(request, template , context) 


def sendmail(request):
    send_mail('This is a Test ','Yes ! we did it',settings.EMAIL_HOST_USER,[settings.EMAIL_TARGET_RECIEVE],fail_silently=False)
    return render(request, 'pages/index.html')



def handle404(request, exception):
    return render(request, 'pages/error.html', status=404)

def handle500(request, exception):
    return render(request, 'pages/error.html', status=500)

    