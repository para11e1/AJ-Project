# Generated by Django 3.1.7 on 2021-05-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='phoneNumber',
            field=models.CharField(default=12233345556, max_length=11),
        ),
    ]