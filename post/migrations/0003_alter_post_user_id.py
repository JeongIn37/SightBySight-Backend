# Generated by Django 3.2.11 on 2022-01-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
