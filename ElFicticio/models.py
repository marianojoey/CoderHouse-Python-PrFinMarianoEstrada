from django.db import models

# Create your models here.

class MNotas (models.Model):
    def __str__(self):
        return f"Título: {self.m_titulo} --- Autor: {self.m_autor} --- Publicado el {self.m_fecha_publ}"

    m_titulo = models.CharField(max_length=25)
    m_descripcion= models.CharField(max_length=60)
    m_autor= models.CharField(max_length=40)
    m_cuerpo= models.TextField()
    m_fecha_publ=models.DateField()

class MPeriodistas (models.Model):
    def __str__(self):
        if self.m_es_editor:
            return f"Periodista: {self.m_nombre_apel} --- E-Mail: {self.m_email} --- ¿Es editor? Sí"
        else:
            return f"Periodista: {self.m_nombre_apel} --- E-Mail: {self.m_email} --- ¿Es editor? No"
        
    m_nombre_apel=models.CharField(max_length=40)
    m_email=models.EmailField()
    m_es_editor=models.BooleanField()
