# Generated by Django 4.2.6 on 2023-10-20 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0012_add_leave_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='add_leave_type',
        ),
        migrations.RemoveField(
            model_name='leavetype',
            name='EmpId',
        ),
        migrations.RemoveField(
            model_name='leavetype',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='leavetype',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='leavetype',
            name='Status',
        ),
    ]
