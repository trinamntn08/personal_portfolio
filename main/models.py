from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Project(models.Model):
    title =  models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image =models.FileField(upload_to='images/',blank=True)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
