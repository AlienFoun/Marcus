from django.db import models


# Create your models here.
class UpgradeDB(models.Model):
    tags = models.CharField(max_length=150, help_text='Enter your tag')
    words = models.TextField(help_text='Enter your words')

    def __str__(self):
        return self.tags
