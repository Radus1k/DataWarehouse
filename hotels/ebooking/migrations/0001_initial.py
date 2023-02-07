# Generated by Django 4.1.5 ON dw_manager.2023-01-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id_camera', models.FloatField(primary_key=True, serialize=False)),
                ('id_hotel', models.FloatField()),
                ('nr_camera', models.FloatField(blank=True, null=True)),
                ('nr_etaj', models.FloatField(blank=True, null=True)),
                ('nr_paturi_duble', models.FloatField()),
                ('nr_paturi_simple', models.FloatField()),
                ('are_terasa', models.BooleanField()),
                ('are_televizor', models.BooleanField()),
                ('pret_per_noapte', models.FloatField()),
            ],
            options={
                'db_table': 'camera',
            },
        ),
        migrations.CreateModel(
            name='Rezervare',
            fields=[
                ('id_rezervare', models.FloatField(primary_key=True, serialize=False)),
                ('id_client', models.FloatField()),
                ('data_inceput', models.DateField()),
                ('data_sfarsit', models.DateField()),
            ],
            options={
                'db_table': 'rezervare',
            },
        ),
        migrations.CreateModel(
            name='Utilizator',
            fields=[
                ('id_utilizator', models.FloatField(primary_key=True, serialize=False)),
                ('nume_utilizator', models.CharField(max_length=30)),
                ('hash_parola', models.CharField(max_length=25)),
                ('nume_complet', models.CharField(max_length=30)),
                ('telefon', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('data_nasterii', models.DateField()),
                ('gen', models.CharField(blank=True, max_length=20, null=True)),
                ('stare_civila', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'utilizator',
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id_zona', models.FloatField(primary_key=True, serialize=False)),
                ('judet', models.CharField(max_length=50)),
                ('localitate', models.CharField(max_length=50)),
                ('pozitie', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'zona',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id_hotel', models.FloatField(primary_key=True, serialize=False)),
                ('nume', models.CharField(max_length=50)),
                ('nr_stele', models.FloatField()),
                ('are_mic_dejun_inclus', models.BooleanField()),
                ('id_zona', models.ForeignKey(db_column='id_zona', on_delete=django.db.models.deletion.DO_NOTHING, to='ebooking.zona')),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='Atribuie',
            fields=[
                ('id_rezervare', models.OneToOneField(db_column='id_rezervare', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ebooking.rezervare')),
                ('id_camera', models.FloatField()),
            ],
            options={
                'db_table': 'atribuie',
                'unique_together': {('id_rezervare', 'id_camera')},
            },
        ),
    ]
