# Generated by Django 3.1.4 on 2021-02-08 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0024_auto_20210205_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='category',
        ),
        migrations.RenameField(
            model_name='f_login',
            old_name='email',
            new_name='femail',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]