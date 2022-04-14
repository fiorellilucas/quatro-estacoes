# Generated by Django 4.0.4 on 2022-04-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id_morador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('bloco', models.CharField(max_length=50)),
                ('apartamento', models.IntegerField()),
                ('interfone', models.IntegerField()),
                ('celular', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sindico', models.BooleanField()),
            ],
        ),
    ]
