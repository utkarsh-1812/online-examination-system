# Generated by Django 4.1.7 on 2023-04-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Question',
            field=models.CharField(max_length=100),
        ),
    ]
