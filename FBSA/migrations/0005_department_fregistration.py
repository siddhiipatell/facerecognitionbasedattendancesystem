# Generated by Django 3.1.4 on 2021-01-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0004_auto_20210102_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fregistration',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
