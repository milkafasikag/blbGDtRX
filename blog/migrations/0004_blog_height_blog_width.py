# Generated by Django 4.2.4 on 2023-11-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
