# Generated by Django 2.1 on 2018-09-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180919_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[(1, 'Customer'), (2, 'Employee'), (3, 'Manager')], max_length=50),
        ),
    ]