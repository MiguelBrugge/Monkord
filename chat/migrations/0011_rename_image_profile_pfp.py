# Generated by Django 4.2.2 on 2023-06-30 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='pfp',
        ),
    ]
