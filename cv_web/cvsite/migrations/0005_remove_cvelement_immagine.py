# Generated by Django 4.1.1 on 2022-09-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0004_alter_cvelement_immagine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvelement',
            name='immagine',
        ),
    ]
