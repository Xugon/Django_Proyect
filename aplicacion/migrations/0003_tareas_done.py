# Generated by Django 5.2.4 on 2025-07-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_tareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
