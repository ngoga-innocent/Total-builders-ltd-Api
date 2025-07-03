from django.contrib import admin
from .models import Services, Project, Testimonial, OurClients,OurTeam,ContactMessage,Quote,ProjectImage

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title',)
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'location', 'duration', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('location', 'created_at')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating')
    search_fields = ('name', 'location', 'message')
    list_filter = ('location', 'rating')

@admin.register(OurClients)
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)
@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    search_fields = ('position',)
@admin.register(ContactMessage)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name',)
admin.site.register(Quote)
