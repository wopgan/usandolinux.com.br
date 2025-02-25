from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from authentication.models import Person

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título:')
    content = RichTextUploadingField(verbose_name="Conteúdo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')
    author = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Autor:')
    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Imagem Thumb:')

    def __str__(self):
        return self.title
