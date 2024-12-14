# Generated by Django 4.1 on 2022-09-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('short_desc', models.CharField(max_length=300, null=True)),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='post_images')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
    ]
