# Generated by Django 4.1.7 on 2023-04-16 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_questionpaper_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]