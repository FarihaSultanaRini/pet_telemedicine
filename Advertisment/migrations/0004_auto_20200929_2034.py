# Generated by Django 3.1.1 on 2020-09-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advertisment', '0003_auto_20200929_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='images/th.jpg', upload_to='images/Advertisement'),
        ),
    ]
