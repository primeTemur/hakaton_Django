from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.db.models import Exists,OuterRef

from .models import Event,Idea,IdeaUpvote
from .forms import CreateIdeaForm


class EventDetailView(View):
    
    def get(self,request,event_id):
        try:
            event=Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse('Event does not exists')
        
        ideas = event.ideas.annotate(
            is_liked=Exists(
                IdeaUpvote.objects.filter(user=request.user, idea=OuterRef("pk"))
            )
        )
        context={
            'event': event,
            'idea_form': CreateIdeaForm(initial={'event': event,'owner': request.user}),
            'ideas': ideas,
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
    
class UpvoteIdeaView(LoginRequiredMixin,View):
    def post(self,request,event_id,idea_id):
    
        try:
            idea=Idea.objects.get(pk=idea_id,event__id=event_id)
        except Idea.DoesNotExist:
            return HttpResponse('Idea does not exists')
        
        IdeaUpvote.objects.create(
            user=request.user,
            idea=idea
        )

        return redirect("events:event-detail", event_id=event_id)
        