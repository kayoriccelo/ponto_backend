# Generated by Django 2.2.4 on 2019-08-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_custom', '0002_usercustom_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercustom',
            name='company',
        ),
        migrations.RemoveField(
            model_name='usercustom',
            name='phone',
        ),
        migrations.AddField(
            model_name='usercustom',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usercustom',
            name='first_access',
            field=models.BooleanField(default=False),
        ),
    ]