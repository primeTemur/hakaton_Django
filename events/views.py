from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from .models import Event,Idea
from .forms import CreateIdeaForm


class EventDetailView(View):
    
    def get(self,request,event_id):
        try:
            event=Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse('Event does not exists')
        
        context={
            'event': event,
            'idea_form': CreateIdeaForm(initial={'event': event,'owner': request.user}),
        }

        return render(request,'events/event_detail.html',context=context)

class CreateEventIdeaView(LoginRequiredMixin,View):
    def post(self,request,event_id):
        try:
            event=Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse('Event does not exists')
        
        form=CreateIdeaForm(request.POST)

        if form.is_valid():
            Idea.objects.create(
                owner=request.user,
                event=event,
                title=form.cleaned_data['title'],
                owerview=form.cleaned_data['owerview'],
            )
        
        return redirect("events:event-detail", event_id=event.id)