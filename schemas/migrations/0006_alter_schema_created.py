# Generated by Django 4.1.7 on 2023-03-22 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0005_alter_schema_created_alter_schema_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='created',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
