# Generated by Django 5.2 on 2025-04-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='stock_symbol',
        ),
        migrations.AddField(
            model_name='alert',
            name='condition',
            field=models.CharField(choices=[('above', 'Above Target Price'), ('below', 'Below Target Price')], default='above', max_length=10),
        ),
    ]
