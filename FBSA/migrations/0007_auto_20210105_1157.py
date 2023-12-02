# Generated by Django 3.1.4 on 2021-01-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0006_auto_20210104_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='f_registration',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]