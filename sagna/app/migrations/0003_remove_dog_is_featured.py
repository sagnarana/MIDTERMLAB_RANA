# Generated by Django 5.0.6 on 2024-06-27 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_dog_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='is_featured',
        ),
    ]