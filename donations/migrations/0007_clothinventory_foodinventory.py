# Generated by Django 4.1 on 2022-09-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_money_donation_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='clothInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt', models.IntegerField(null=True)),
                ('pant', models.IntegerField(null=True)),
                ('t_shirt', models.IntegerField(null=True)),
                ('vest', models.IntegerField(null=True)),
                ('lungi', models.IntegerField(null=True)),
                ('salwar', models.IntegerField(null=True)),
                ('pajama', models.IntegerField(null=True)),
                ('saree', models.IntegerField(null=True)),
                ('punjabi', models.IntegerField(null=True)),
                ('blanket', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='foodInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_people', models.IntegerField(null=True)),
            ],
        ),
    ]
