from ckeditor.fields import RichTextField
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
