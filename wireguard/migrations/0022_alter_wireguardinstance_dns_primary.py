# Generated by Django 5.0.2 on 2024-03-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wireguard', '0021_remove_peerallowedip_missing_from_wireguard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wireguardinstance',
            name='dns_primary',
            field=models.GenericIPAddressField(blank=True, default='1.1.1.1', null=True, protocol='IPv4'),
        ),
    ]