# Generated by Django 4.0.5 on 2022-06-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_plans_id_alter_plans_planid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='planId',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
