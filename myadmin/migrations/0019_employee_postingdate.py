# Generated by Django 4.2.6 on 2023-10-24 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0018_rename_emocode_employee_empcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='PostingDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
