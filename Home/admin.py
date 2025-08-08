from django.contrib import admin
from . import models


# Custom admin branding
admin.site.site_header = "Shree Rastriya Secondary School Admin Site"
admin.site.site_title = "Shree Rastriya Secondary School Admin Portal"
admin.site.index_title = "Welcome to Shree Rastriya Secondary School Admin Dashboard"


# Register your models here.

# tile 
admin.site.register(models.Header)
#slide show

admin.site.register(models.Slider)

admin.site.register(models.News)

admin.site.register(models.Event)

admin.site.register(models.GalleryImage)

admin.site.register(models.Achievements)

admin.site.register(models.Academics)

admin.site.register(models.Head_faculty)

admin.site.register(models.Academic_resources)

admin.site.register(models.Contact)

admin.site.register(models.Members)