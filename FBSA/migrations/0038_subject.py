# Generated by Django 3.1.4 on 2021-03-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0037_s_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=20)),
            ],
        ),
    ]
