from django.shortcuts import render, redirect

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
    return "df"