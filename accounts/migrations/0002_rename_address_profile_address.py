# Generated by Django 4.0.6 on 2022-08-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Address',
            new_name='address',
        ),
    ]
