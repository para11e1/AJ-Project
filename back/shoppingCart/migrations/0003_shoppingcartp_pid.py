# Generated by Django 3.1.7 on 2021-05-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0002_auto_20210508_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcartp',
            name='pid',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
