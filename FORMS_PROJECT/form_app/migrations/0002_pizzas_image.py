# Generated by Django 3.0.7 on 2020-07-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzas',
            name='image',
            field=models.ImageField(default=2, upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]
