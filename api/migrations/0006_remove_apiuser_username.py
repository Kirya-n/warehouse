# Generated by Django 5.0.1 on 2024-01-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_apiuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiuser',
            name='username',
        ),
    ]
