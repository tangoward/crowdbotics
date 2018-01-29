from django.contrib import admin
from .models import Dog, Cat
# Register your models here.


class DogAdmin(admin.ModelAdmin):
    pass


class CatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dog)
admin.site.register(Cat)
