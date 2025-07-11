# Generated by Django 5.2 on 2025-06-14 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('condition', models.CharField(choices=[('above', 'Above Target Price'), ('below', 'Below Target Price')], default='above', max_length=10)),
                ('is_triggered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('triggered_at', models.DateTimeField(blank=True, null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='stocks.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
