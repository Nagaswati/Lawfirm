# Generated by Django 3.2.7 on 2022-04-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('current', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'lawyer',
            },
        ),
    ]
