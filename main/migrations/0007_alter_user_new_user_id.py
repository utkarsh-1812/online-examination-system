# Generated by Django 4.1.7 on 2023-04-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_user_new_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_new',
            name='User_ID',
            field=models.CharField(default='8dd31245d60d4b7ea414ed61fd7758ca', max_length=100, unique=True),
        ),
    ]
