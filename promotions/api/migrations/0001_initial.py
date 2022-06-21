# Generated by Django 4.0.5 on 2022-06-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planId', models.IntegerField()),
                ('planName', models.CharField(max_length=100)),
                ('amounts', models.FloatField()),
                ('tenure', models.DurationField()),
                ('benifitPercentage', models.FloatField()),
                ('benifitTypes', models.CharField(choices=[('Cashback', 'Cashback'), ('ExtraVoucher', 'ExtraVoucher')], default='ExtraVoucher', max_length=100)),
            ],
        ),
    ]
