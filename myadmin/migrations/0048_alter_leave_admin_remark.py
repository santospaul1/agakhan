# Generated by Django 4.2.6 on 2023-11-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0047_alter_leave_admin_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='admin_remark',
            field=models.CharField(default=None, max_length=255),
        ),
    ]