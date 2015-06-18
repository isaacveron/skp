# django imports
from django.core.urlresolvers import reverse
from django.db import models

# third party imports
from db_file_storage.model_utils import delete_file, delete_file_if_needed


class Documento(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Document(models.Model):
    name = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=False)
    docfile = models.FileField(
        upload_to='archivos.Documento/bytes/filename/mimetype',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('document.edit', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'docfile')
        super(Document, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Document, self).delete(*args, **kwargs)
        delete_file(self, 'docfile')