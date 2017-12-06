from django.contrib import admin

# Register your models here.
from .models import Status
from .models import User
from .models import Landmark

admin.site.register(Status)
admin.site.register(User)
admin.site.register(Landmark)