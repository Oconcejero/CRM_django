from django.contrib import admin

admin.site.unregister(admin.models.Group)
admin.site.unregister(admin.models.User)
