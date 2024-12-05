# Generated by Django 5.0.7 on 2024-11-28 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_asiganimalfoodmove_asiganimalmove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asiganimalfoodmove',
            name='animalfood_move',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.animalfoodmove'),
        ),
        migrations.AlterField(
            model_name='asiganimalmove',
            name='animal_move',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.animalmove'),
        ),
    ]