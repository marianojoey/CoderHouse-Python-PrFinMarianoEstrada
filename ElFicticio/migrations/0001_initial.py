# Generated by Django 4.1.5 on 2023-02-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MNotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_titulo', models.CharField(max_length=25)),
                ('m_descripcion', models.CharField(max_length=60)),
                ('m_autor', models.CharField(max_length=40)),
                ('m_cuerpo', models.TextField()),
                ('m_fecha_publ', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MPeriodistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_nombre_apel', models.CharField(max_length=40)),
                ('m_email', models.EmailField(max_length=254)),
                ('m_es_editor', models.BooleanField()),
            ],
        ),
    ]
