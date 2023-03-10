# Generated by Django 4.1.5 on 2023-01-15 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('state', models.CharField(max_length=255, verbose_name='Должность')),
                ('start_date', models.DateField(verbose_name='Дата приема')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='apiapp.topmanager', verbose_name='Начальник')),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('state', models.CharField(max_length=255, verbose_name='Должность')),
                ('start_date', models.DateField(verbose_name='Дата приема')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='apiapp.manager', verbose_name='Начальник')),
            ],
        ),
    ]
