# Generated by Django 3.2.12 on 2023-10-13 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0004_alter_computergeneration_generation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computergeneration',
            old_name='RAM',
            new_name='ram',
        ),
    ]
