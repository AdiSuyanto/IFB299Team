# Generated by Django 2.1 on 2018-09-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_state',
            field=models.CharField(choices=[('New South Wales', 'New South Wales'), ('Queensland', 'Queensland'), ('South Australia', 'South Australia'), ('Victoria', 'Victoria'), ('Tasmania', 'Tasmania')], max_length=50),
        ),
    ]
