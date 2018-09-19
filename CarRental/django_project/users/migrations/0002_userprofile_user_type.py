# Generated by Django 2.1 on 2018-09-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[(1, 'Customer'), (2, 'Employee'), (3, 'Manager')], default='Employee', max_length=50),
        ),
    ]
