# Generated by Django 3.2.20 on 2023-07-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('comision', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('profesion', models.CharField(max_length=128)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
