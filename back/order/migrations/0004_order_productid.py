# Generated by Django 3.1.7 on 2021-05-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210524_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]