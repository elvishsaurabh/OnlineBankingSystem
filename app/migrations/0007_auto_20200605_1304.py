# Generated by Django 3.0.6 on 2020-06-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200605_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_history',
            name='Reciever',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction_history',
            name='Sender',
            field=models.IntegerField(null=True),
        ),
    ]
