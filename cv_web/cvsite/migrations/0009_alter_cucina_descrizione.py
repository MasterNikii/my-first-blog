# Generated by Django 4.1.1 on 2022-10-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0008_cucina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cucina',
            name='descrizione',
            field=models.CharField(default=None, max_length=10000),
        ),
    ]
