# Generated by Django 3.1.1 on 2020-09-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, default='images/th.jpg', null=True, upload_to='images/Houes'),
        ),
    ]
