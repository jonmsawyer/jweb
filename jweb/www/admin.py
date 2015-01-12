from django.contrib import admin

from www.models import Copyright, Home

class CopyrightAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ("title",)}
    pass
admin.site.register(Copyright, CopyrightAdmin)

class HomeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Home, HomeAdmin)

