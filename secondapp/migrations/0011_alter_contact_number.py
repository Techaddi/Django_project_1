# Generated by Django 3.2.4 on 2021-06-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0010_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]