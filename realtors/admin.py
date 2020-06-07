from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    
    # def admin_image(self, obj):
        # return mark_safe('<img src="%s" />' % obj.photo)
     
    # admin_image.allow_tags = True

admin.site.register(Realtor, RealtorAdmin)
