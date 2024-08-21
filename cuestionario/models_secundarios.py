from django.db import models
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo tags               #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#

class Tags(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    class Meta:
        ordering = ["-id"]

        verbose_name = "Tag"

        verbose_name_plural = "Tags"

        db_table = "Tag"
    
    def __str__(self):
        return self.titulo