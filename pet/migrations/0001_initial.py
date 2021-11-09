# Generated by Django 3.2.6 on 2021-09-04 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=3)),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=100)),
                ('weight', models.FloatField(max_length=100)),
                ('image', models.ImageField(blank=True, default='images/thh.jpg', upload_to='images/Houes')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
