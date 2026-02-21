from django.contrib import admin
from .models import  Sermon,  GalleryImage
from .models import *

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "folder", "uploaded_by")
    readonly_fields = ("uploaded_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # only set uploaded_by on creation
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(GalleryFolder)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(ContactMessage)
admin.site.register(DailyVerse)
admin.site.register(Sermon)
admin.site.register(Meeting)
