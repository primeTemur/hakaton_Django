from django.contrib import admin

from .models import Event,Idea

class EventAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'organizer',
        'start_date',
        'end_date',
        'is_approved',
    )
admin.site.register(Event,EventAdmin)

class IdeaAdmin(admin.ModelAdmin):
    list_display=(
        'event',
        'owner',
        'title',
        'owerview'
    )
admin.site.register(Idea,IdeaAdmin)