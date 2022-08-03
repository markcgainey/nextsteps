# Generated by Django 4.0.6 on 2022-07-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='johndoe@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(default='john', max_length=250),
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(default='doe', max_length=250),
        ),
    ]
