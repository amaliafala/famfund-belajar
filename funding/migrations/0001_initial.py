# Generated by Django 4.0.3 on 2022-03-05 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asisten',
            fields=[
                ('nim', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('tagihan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal', models.IntegerField()),
                ('tanggal_bayar', models.DateTimeField()),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asisten', to='funding.asisten')),
            ],
        ),
    ]
