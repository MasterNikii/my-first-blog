# Generated by Django 4.1.1 on 2022-09-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0002_alter_cvelement_descrizione_alter_cvelement_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvelement',
            name='immagine',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
