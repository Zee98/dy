from django.contrib import admin
from website.models import Sms, Subscriberlist, Profile, Post, Member

admin.site.site_header = "Dyanmic Youth of Afghanistan Organization "
admin.site.site_title = "DYAO"
admin.site.index_title = "Weelcome to Admin page"
admin.site.register(Sms)
admin.site.register(Subscriberlist)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Member)