# Generated by Django 5.0.2 on 2024-03-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wireguard', '0019_alter_wireguardinstance_legacy_firewall'),
    ]

    operations = [
        migrations.AddField(
            model_name='peerallowedip',
            name='config_file',
            field=models.CharField(choices=[('server', 'Server Config'), ('client', 'Client config')], default='server', max_length=6),
        ),
    ]