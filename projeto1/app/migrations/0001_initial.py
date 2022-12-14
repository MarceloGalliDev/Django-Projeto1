# Generated by Django 4.1.4 on 2022-12-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Programado'), (2, 'Desenvolvendo'), (3, 'Concluído')])),
            ],
        ),
    ]
