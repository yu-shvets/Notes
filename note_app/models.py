from django.db import models
from encrypted_id.models import EncryptedIDModel

# Create your models here.


class Notes(EncryptedIDModel):

    class Meta(object):
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ['-datetime']

    note = models.TextField(blank=False)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.datetime)
