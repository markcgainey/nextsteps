# Generated by Django 4.0.6 on 2022-07-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0003_member_know_god'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='know_god',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
