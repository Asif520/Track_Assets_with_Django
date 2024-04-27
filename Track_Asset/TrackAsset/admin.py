from django.contrib import admin

# Register your models here.
from .models import User,Company,Company_Assets,Subscriber


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Company_Assets)
admin.site.register(Subscriber)
