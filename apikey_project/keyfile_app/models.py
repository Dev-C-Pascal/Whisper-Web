from django.db import models


class ApiKey(models.Model):
    key = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploaded_files/', blank=True, null=True)

    def __str__(self):
        return self.key

