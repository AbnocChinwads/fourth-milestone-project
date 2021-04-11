from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
