# Generated by Django 4.2.2 on 2023-06-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_handle_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='online',
            field=models.BooleanField(default=True),
        ),
    ]
