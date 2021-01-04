from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Document, DocumentAdmin)
