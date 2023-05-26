from django.contrib import admin

from advertisements.models import Advertisement

# Register your models here.

#admin.site.register(Advertisement)


@admin.register(Advertisement)
class AdAdmin(admin.ModelAdmin):
    pass
