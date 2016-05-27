from django.contrib import admin

from .models import Dog, NickNames   

class NickNamesInline(admin.TabularInline):
    model = NickNames
    extra = 3


class DogAdmin(admin.ModelAdmin):
    inlines = [NickNamesInline]

admin.site.register(Dog, DogAdmin)
