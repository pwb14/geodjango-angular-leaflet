# Generated by Django 3.0.3 on 2020-02-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldborder',
            name='fips',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='FIPS Code'),
        ),
    ]
