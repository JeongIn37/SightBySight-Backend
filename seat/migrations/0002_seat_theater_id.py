# Generated by Django 3.2.11 on 2022-01-17 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0001_initial'),
        ('seat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='theater_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.theater'),
        ),
    ]
