from django.contrib import admin
from .models import Artist, Album
class ArtistAdmin(admin.ModelAdmin):
    pass

admin.site.register([Artist, Album], ArtistAdmin)

