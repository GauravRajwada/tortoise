# Generated by Django 4.0.5 on 2022-06-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='id',
        ),
        migrations.AlterField(
            model_name='plans',
            name='planId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plans',
            name='tenure',
            field=models.CharField(max_length=100),
        ),
    ]
