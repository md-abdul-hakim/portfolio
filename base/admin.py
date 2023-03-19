from django.contrib import admin
from .models import (
    Profile, About, Service, Location,
    Skill, Education, Experience, Message,
    Category, Blog
    )


# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Message)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Blog)

