from django.contrib import admin
from steps.models import Member, Know, Connect, Grow, Change

# Register your models here.
admin.site.register(Member)
admin.site.register(Know)
admin.site.register(Connect)
admin.site.register(Grow)
admin.site.register(Change)