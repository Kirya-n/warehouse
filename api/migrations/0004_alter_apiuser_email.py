# Generated by Django 5.0.1 on 2024-01-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_apiuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
