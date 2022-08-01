from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class VideoTag(models.Model):
    """
    Youtube Video Tag Model
    Defines the attributes of tags of an youtube video
    """
    tag = models.CharField(_("Tag"), unique=True, max_length=128)
    
    class Meta:
        verbose_name = _("Video Tag")
        verbose_name_plural = _("Video Tags")

    def __str__(self):
        return self.tag
    
class YoutubeVideo(models.Model):
    """
    Youtube Video Model
    Defines the attributes of an youtube video
    """
    title = models.CharField(_("Title"), max_length=128)
    id = models.CharField(_("ID"), max_length=128,primary_key=True)
    url = models.CharField(_("URL"), max_length=128)
    duration = models.IntegerField(_("Duration"))
    view_count = models.IntegerField(_("View Count"), max_length=None)
    thumbnail = models.CharField(_("Thumbnail"), max_length=128)
    tag = models.ManyToManyField(VideoTag, verbose_name=_("Tag"), related_name='youtubeVideo')
    
    class Meta:
        verbose_name = _("Youtube Video")
        verbose_name_plural = _("Youtube Videos")

    def __str__(self):
        return self.title