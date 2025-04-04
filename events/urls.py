from django.urls import path

from .views import EventDetailView

app_name="events"
urlpatterns = [
    path(""),
    path('<int:event_id>/', EventDetailView.as_view(),name='event-detail'),
]
