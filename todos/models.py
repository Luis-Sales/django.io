from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField( verbose_name="Data de Criação" ,null=False, blank=False)
    finshed_at = models.DateField(null=True)
    
    
