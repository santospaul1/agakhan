# Generated by Django 4.2.6 on 2023-10-26 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='empid',
        ),
        migrations.DeleteModel(
            name='LeaveType',
        ),
        migrations.DeleteModel(
            name='Leave',
        ),
    ]
