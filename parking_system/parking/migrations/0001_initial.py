# Generated by Django 3.0.5 on 2020-08-20 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import parking.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(choices=[('Bike', 'Bike'), ('Car', 'Car'), ('Bicycle', 'Bicycle')], default='Car', max_length=20)),
                ('logs', djongo.models.fields.EmbeddedField(model_container=parking.models.Log, null=True)),
                ('slot', models.PositiveIntegerField()),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parking',
                'verbose_name_plural': 'Parkings',
            },
        ),
    ]
