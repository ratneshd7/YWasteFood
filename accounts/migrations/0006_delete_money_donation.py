# Generated by Django 4.0.6 on 2022-08-20 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_money_donation_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='money_donation',
        ),
    ]
