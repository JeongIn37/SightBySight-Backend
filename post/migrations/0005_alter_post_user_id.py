# Generated by Django 3.2.11 on 2022-01-18 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0001_initial'),
        ('post', '0004_alter_post_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='userAccount.user'),
        ),
    ]
