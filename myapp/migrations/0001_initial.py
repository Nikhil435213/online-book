# Generated by Django 4.0 on 2022-03-09 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('cust_id', models.IntegerField(primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=0)),
                ('open_date', models.DateField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('trans_id', models.IntegerField(primary_key=True, serialize=False)),
                ('recevr', models.IntegerField(default=0)),
                ('val', models.FloatField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
                ('dat', models.DateField(default=0)),
                ('sendr', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.cust')),
            ],
        ),
    ]
