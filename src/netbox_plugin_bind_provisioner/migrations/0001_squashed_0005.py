import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Squash of migrations 0001-0005. Replaces the original chain which had
    hard dependencies on netbox extras>=0133 (netbox 4.5) and
    netbox_dns>=0030 (netbox-plugin-dns 1.5.0).

    This squashed migration is compatible with netbox-plugin-dns>=1.2.14
    (netbox 4.2+) by depending only on the initial netbox_dns migration.
    """

    replaces = [
        ('netbox_plugin_bind_provisioner', '0001_initial'),
        ('netbox_plugin_bind_provisioner', '0002_alter_integerkeyvaluesetting_options_and_more'),
        ('netbox_plugin_bind_provisioner', '0003_catalogzonememberidentifier'),
        ('netbox_plugin_bind_provisioner', '0004_alter_catalogzonememberidentifier_zone'),
        ('netbox_plugin_bind_provisioner', '0005_alter_catalogzonememberidentifier_zone'),
    ]

    dependencies = [
        ('netbox_dns', '0001_squashed_netbox_dns_0_22'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegerKeyValueSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=64)),
                ('value', models.IntegerField()),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='CatalogZoneMemberIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=26, unique=True)),
                ('zone', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='catz_identifier',
                    to='netbox_dns.zone',
                )),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
