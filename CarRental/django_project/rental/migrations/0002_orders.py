# Generated by Django 2.1 on 2018-09-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(db_column='Order_ID', primary_key=True, serialize=False)),
                ('order_createdate', models.IntegerField(db_column='Order_CreateDate')),
                ('order_pickupdate', models.IntegerField(db_column='Order_PickupDate')),
                ('order_pickupstore', models.IntegerField(db_column='Order_PickupStore')),
                ('pickup_store_name', models.CharField(blank=True, db_column='Pickup_Store_Name', max_length=25, null=True)),
                ('pickup_store_address', models.CharField(blank=True, db_column='Pickup_Store_Address', max_length=25, null=True)),
                ('pickup_store_phone', models.CharField(blank=True, db_column='Pickup_Store_Phone', max_length=25, null=True)),
                ('pickup_store_city', models.CharField(blank=True, db_column='Pickup_Store_City', max_length=45, null=True)),
                ('pickup_store_state_name', models.CharField(blank=True, db_column='Pickup_Store_State_Name', max_length=25, null=True)),
                ('order_returndate', models.IntegerField(db_column='Order_ReturnDate')),
                ('order_returnstore', models.IntegerField(db_column='Order_ReturnStore')),
                ('return_store_name', models.CharField(blank=True, db_column='Return_Store_Name', max_length=25, null=True)),
                ('return_store_address', models.CharField(blank=True, db_column='Return_Store_Address', max_length=25, null=True)),
                ('return_store_phone', models.CharField(blank=True, db_column='Return_Store_Phone', max_length=25, null=True)),
                ('return_store_city', models.CharField(blank=True, db_column='Return_Store_City', max_length=45, null=True)),
                ('return_store_state', models.CharField(blank=True, db_column='Return_Store_State', max_length=25, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]
