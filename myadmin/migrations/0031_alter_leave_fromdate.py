# Generated by Django 4.2.6 on 2023-10-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0030_leave_fromdate_leave_todate_alter_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='fromdate',
            field=models.DateField(auto_now=True),
        ),
    ]
