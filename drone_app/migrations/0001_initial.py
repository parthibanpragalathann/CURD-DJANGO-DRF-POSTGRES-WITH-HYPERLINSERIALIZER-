# Generated by Django 3.2.7 on 2021-09-16 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DronesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pilots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Transgender')])),
                ('number_race', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacture_date', models.DateField()),
                ('is_participated', models.CharField(choices=[('participate', 'Participate'), ('not participate', 'Not Participate')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('drone_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_app.dronescategory')),
            ],
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_app.drones')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_app.pilots')),
            ],
        ),
    ]
