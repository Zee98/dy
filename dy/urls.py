"""dy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views
from website.views import PostlistView, PostDetailView, MemberViewList, IndexViewList
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexViewList.as_view(), name="index"),
    path("blog", PostlistView.as_view(), name="blog"),
    path("blog/<int:pk>", PostDetailView.as_view(), name="blog-detail"),
    path("contact", views.contact, name="contact"),
    path("initiatives", views.initiatives, name="initiatives"),
    path("report", views.report, name="report"),
    path("team", MemberViewList.as_view(), name="team"),
    path("about", views.about, name="about"),
    path("contact/sms", views.sms, name="sms"),
    path('subscribed', views.subscriber , name='subscribe'),
    # path('post', views.post, name = 'post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
