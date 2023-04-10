# Generated by Django 4.2 on 2023-04-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('energy_reading', models.FloatField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
