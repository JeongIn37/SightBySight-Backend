# Generated by Django 3.2.11 on 2022-01-16 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
