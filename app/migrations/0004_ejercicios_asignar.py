# Generated by Django 3.1.2 on 2022-06-28 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_quequieres'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicios',
            name='asignar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.quequieres'),
            preserve_default=False,
        ),
    ]
