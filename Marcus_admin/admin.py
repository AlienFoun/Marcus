from django.contrib import admin
from .models import UpgradeDB
from study import update_problems_dict
from helper import sanitizer
from sql import con


# Register your models here.

class UpgradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags', 'words')
    list_display_links = ('id',)
    search_fields = ('id', 'tags', 'words')
    list_editable = ('tags', 'words')

    def save_model(self, request, obj, form, change):
        sanitized_text = sanitizer(obj.words)
        con.ping()

        update_problems_dict(sanitized_text, obj.tags)
        super().save_model(request, obj, form, change)


admin.site.register(UpgradeDB, UpgradeAdmin)
