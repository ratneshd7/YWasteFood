# Generated by Django 4.1 on 2022-09-04 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_post_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='postMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='post_images')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('post_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
    ]
