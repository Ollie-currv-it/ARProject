from django.db import models

# Create your models here.

class UploadedModelFile(models.Model):
    model_file = models.FileField(upload_to='uploaded_models/')
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField()
    tags = models.JSONField(default=list, blank=True)  # List of tags to describe the model
    model_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.model_name
