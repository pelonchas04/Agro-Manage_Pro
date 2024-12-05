# Generated by Django 5.0.7 on 2024-11-05 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cages', '0002_alter_cage_id_alter_feedanimal_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cage',
            name='name',
            field=models.CharField(default='', max_length=30, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]