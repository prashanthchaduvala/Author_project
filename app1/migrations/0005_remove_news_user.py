# Generated by Django 3.1.3 on 2021-01-26 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
    ]
