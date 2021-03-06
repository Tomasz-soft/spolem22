# Generated by Django 3.1.7 on 2021-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Towary',
            fields=[
                ('status', models.IntegerField()),
                ('id_tow', models.IntegerField(primary_key=True, serialize=False)),
                ('id_gtow', models.IntegerField()),
                ('id_dtow', models.IntegerField()),
                ('id_branz', models.IntegerField()),
                ('atribs_tow', models.IntegerField()),
                ('naz_kas_tow', models.CharField(max_length=25)),
                ('nazwa_tow', models.CharField(max_length=40)),
                ('ident_tow', models.CharField(max_length=13)),
                ('bar_kod_tow', models.CharField(max_length=13)),
                ('gr_rabat_t', models.IntegerField()),
            ],
            options={
                'db_table': 'towary',
                'managed': False,
            },
        ),
    ]
