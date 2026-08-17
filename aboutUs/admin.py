from django.contrib import admin
from aboutUs.models import About,SocialLink


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if(count):
            return False
        else:
            return True

# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)