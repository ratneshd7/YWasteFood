# Generated by Django 4.1 on 2022-09-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image_alter_postmedia_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='image',
            field=models.ImageField(default='default_post.jpg', upload_to='media_images'),
        ),
    ]
