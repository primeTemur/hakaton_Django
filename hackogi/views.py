from django.shortcuts import render
from django.utils import timezone
from events.models import Event

def home_page(request):
    now=timezone.now()
    active_hackathons=Event.objects.filter(
        is_approved=True,
        start_date__lt=now,
        end_date__gt=now
        )
    
    return render(request,'home.html',context={
        'active_hackatons':active_hackathons
    })