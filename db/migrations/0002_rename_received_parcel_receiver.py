# Generated by Django 4.2.6 on 2023-10-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='received',
            new_name='receiver',
        ),
    ]
