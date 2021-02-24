from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
# from website.forms import SMS
from website.models import Sms, Subscriberlist, Post, Member
from django.views.generic import ListView, DetailView

class IndexViewList(ListView):
    model = Member
    context_object_name = 'objects'
    template_name = 'index.html'

class PostlistView(ListView):
    
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class MemberViewList(ListView):
    model = Member
    context_object_name = 'objects'
    template_name = 'team.html' 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# def blog(request):
#     data = {
#         'posts': Post.objects.all()
#     }
#     return render(request, "blog.html", data)

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

def post(request, id=2):
    data = {
        'post': Post.objects.get(pk=id)
    }
    return render(request, "post.html", data)


def subscriber(request):
    myemail = request.POST.get('email')
    sub = Subscriberlist(email=myemail)
    sub.save()
    messages.success(request, 'Thank you for subscribing. you will recieve our updates on your email.')
    return render(request, 'subscriber.html')


def sms(request):
    username = request.POST.get('name')
    useremail = request.POST.get('email')
    usermessage = request.POST.get('message')
    me = Sms(name=username, email=useremail, message=usermessage)
    me.save()
    messages.success(request, 'Thank you, We have got your message.')
    return render(request, 'contact.html')

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
