# Generated by Django 2.1 on 2018-09-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]