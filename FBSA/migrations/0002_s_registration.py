# Generated by Django 3.1.4 on 2021-01-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_registration',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_fname', models.CharField(default=' ', max_length=50)),
                ('s_lname', models.CharField(default=' ', max_length=50)),
                ('subject', models.CharField(default=' ', max_length=100)),
                ('department', models.IntegerField()),
                ('s_sem', models.IntegerField()),
                ('b_date', models.DateField()),
                ('gender', models.CharField(default='boolChoice', max_length=1)),
                ('email', models.EmailField(default=' ', max_length=50)),
                ('c_no', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('c_pass', models.CharField(max_length=50)),
            ],
        ),
    ]