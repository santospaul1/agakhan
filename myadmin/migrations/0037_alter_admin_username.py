# Generated by Django 4.2.6 on 2023-10-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0036_rename_leavetype_leavetype_leavetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
