# Generated by Django 3.1.5 on 2021-01-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0005_auto_20210114_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='food_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='menu/'),
        ),
    ]