# Generated by Django 3.2.5 on 2021-07-12 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_addbooks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addbooks',
            old_name='about',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='addbooks',
            old_name='name',
            new_name='title',
        ),
    ]
