# Generated by Django 4.0 on 2023-06-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisprudencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('fuente', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
            ],
        ),
    ]
