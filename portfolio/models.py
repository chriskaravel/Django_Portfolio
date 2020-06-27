from django.db import models

# Create your models here.

class Script(models.Model):
    name = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField(null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added']