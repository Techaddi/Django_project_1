from django.contrib import admin
from .models import Dest, Message, Service, Contact

admin.site.register(Dest),
admin.site.register(Message),
admin.site.register(Service),
admin.site.register(Contact)

# Register your models here.
