# Generated by Django 5.0 on 2024-01-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADsPartner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
