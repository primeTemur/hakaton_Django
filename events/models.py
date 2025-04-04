from django.db import models
from common.models import BaseModel

from django.utils.translation import gettext_lazy as _

class Event(BaseModel):
    organizer=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE,
                                related_name='events',related_query_name='event')

    title=models.CharField(_("title"),max_length=255)
    overview=models.TextField(_("overview"))

    start_date=models.DateTimeField(_("start date"))
    end_date=models.DateTimeField(_("end date"))

    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Idea(BaseModel):
    event=models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='ideas',
        related_query_name='idea'
    )
    owner=models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='ideas',
        related_query_name='idea'    
    )

    title=models.CharField(_('title'),max_length=250)
    owerview=models.TextField(_('overview'))

    def __str__(self):
        return self.title

class IdeaUpvote(BaseModel):
    idea=models.ForeignKey(
        Idea,
        related_name='upvotes',
        related_query_name='upvote',
        on_delete=models.CASCADE
    )
    user=models.ForeignKey(
        'accounts.CustomUser',
        related_name='upvotes',
        related_query_name='upvote',
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ('idea', 'user')
        verbose_name = _('Idea Upvote')
        verbose_name_plural = _('Idea Upvotes')
    def __str__(self):
        return f'{self.user.username} upvoted {self.idea.title}'

    