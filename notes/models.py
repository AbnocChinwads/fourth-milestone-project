from django.db import models


class Document(models.Model):
    readonly_fields = ('id',)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
