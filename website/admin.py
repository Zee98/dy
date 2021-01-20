from django.contrib import admin
from website.models import Sms, Subscriberlist, Profile, Post, Member

admin.site.register(Sms)
admin.site.register(Subscriberlist)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Member)