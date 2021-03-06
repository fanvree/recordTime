# Generated by Django 3.2.5 on 2021-07-11 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdTime', models.FloatField(default=0)),
                ('visualTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.CharField(default='test', max_length=200)),
                ('keyword', models.CharField(default='', max_length=1000)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
    ]
