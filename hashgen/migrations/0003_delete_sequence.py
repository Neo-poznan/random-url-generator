# Generated by Django 4.2 on 2024-05-28 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashgen', '0002_alter_sequence_num'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sequence',
        ),
    ]
