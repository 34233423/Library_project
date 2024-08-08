# articles/models.py
from django.db import models
from .ocr import extract_text_from_image

class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)  # Title will be auto-extracted
    author = models.CharField(max_length=255, blank=True, null=True)  # Author will be auto-extracted
    front_page_image = models.ImageField(upload_to='articles/images/', null=True, blank=True)
    full_pdf = models.FileField(upload_to='articles/pdfs/')
    content = models.TextField(blank=True, null=True)  # Extracted text content

    def save(self, *args, **kwargs):
        if self.front_page_image:
            self.content = extract_text_from_image(self.front_page_image.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else "Untitled Article"
