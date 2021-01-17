from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from website.forms import SMS

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def initiatives(request):
    return render(request, "initiatives.html")

def report(request):
    return render(request, "report.html")

def team(request):
    return render(request, "team.html")


def sms(request):
    # form = SMS(request.POST)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, 'Thank you, We have got your message.')
    #     return redirect('sms')
    messages.success(request, 'mesage not gotten')
    return redirect('contact')



#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     message = request.POST.get('message')
#     title = 'A message from website'
#     send_mail(
#         title,
#         message,
#         email,
#         ['zamanehsani@gmail.com', 'zamanehsani@yahoo.com'],
#     fail_silently=False,
# )
    