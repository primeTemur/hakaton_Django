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
    past_hackatons=Event.objects.filter(
        is_approved=True,
        end_date__lt=now
    )

    upcoming_hackatons=Event.objects.filter(
        is_approved=True,
        start_date__gt=now
    )

    return render(request,'home.html',context={
        'active_hackatons':active_hackathons,
        'upcoming_hackathons':upcoming_hackatons,
        'past_hackathons':past_hackatons,
    })