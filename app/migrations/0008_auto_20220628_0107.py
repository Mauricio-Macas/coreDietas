# Generated by Django 3.1.2 on 2022-06-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220628_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejercicios',
            name='asignar',
        ),
        migrations.AddField(
            model_name='quequieres',
            name='elige',
            field=models.ManyToManyField(to='app.Ejercicios'),
        ),
    ]
