# Generated by Django 2.2.5 on 2019-10-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20191007_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='image_map',
            field=models.FileField(default=' ', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='myapp',
            name='video_map',
            field=models.FileField(default=' ', upload_to='videos/'),
        ),
    ]
