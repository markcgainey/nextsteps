# Generated by Django 4.0.6 on 2022-07-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0004_alter_member_know_god'),
    ]

    operations = [
        migrations.CreateModel(
            name='Know',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Know God', max_length=250)),
                ('attend_worship_service', models.BooleanField()),
                ('starting_point', models.BooleanField()),
                ('commit_life_to_christ', models.BooleanField()),
                ('recommit_life_to_christ', models.BooleanField()),
                ('baptism', models.BooleanField()),
                ('join_the_church', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='attend_service',
        ),
        migrations.RemoveField(
            model_name='member',
            name='know_god',
        ),
    ]
