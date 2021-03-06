# Generated by Django 2.2.5 on 2019-10-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_myapp_description_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.IntegerField()),
                ('descriptionPlace', models.CharField(max_length=100000)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'description',
            },
        ),
    ]
