
from django.contrib import admin

# Register your models here.
from.models import  Contact, Post,Comment #CategoryAcc,
#  Project,Review,Tag,registerEnquiry,Profile

# admin.site.register(Project)
# admin.site.register(Review)
# admin.site.register(Tag)
# admin.site.register(registerEnquiry)
# admin.site.register(Profile)
admin.site.register(Post)
# admin.site.register(CategoryAcc)
admin.site.register(Comment)
admin.site.register(Contact)