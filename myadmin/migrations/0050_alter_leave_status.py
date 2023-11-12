# Generated by Django 4.2.6 on 2023-11-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0049_alter_leave_admin_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=10),
        ),
    ]
