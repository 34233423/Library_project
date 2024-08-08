# Generated by Django 5.0.7 on 2024-08-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_file',
            new_name='front_page_image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='pdf_file',
            new_name='full_pdf',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
