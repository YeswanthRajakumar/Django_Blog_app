# Generated by Django 3.0.4 on 2020-04-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_pic.png', upload_to='profile_pics'),
        ),
    ]