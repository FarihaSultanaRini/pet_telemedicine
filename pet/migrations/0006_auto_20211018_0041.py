# Generated by Django 3.1.1 on 2021-10-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_alter_pet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
