# Generated by Django 4.0.4 on 2022-05-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quatroestacoes', '0004_alter_reserva_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reuniao',
            name='data',
            field=models.DateTimeField(unique=True, verbose_name='Data e horário da reunião'),
        ),
    ]
