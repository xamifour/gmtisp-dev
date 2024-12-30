# Generated by Django 3.0.7 on 2020-10-02 20:09

from django.db import migrations, models

from openwisp_radius.base.models import _GET_MOBILE_PREFIX_HELP_TEXT


class Migration(migrations.Migration):
    dependencies = [
        ('gmtisp_radius', '0003_default_groups_and_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationradiussettings',
            name='allowed_mobile_prefixes',
            field=models.TextField(
                blank=True,
                help_text=str(_GET_MOBILE_PREFIX_HELP_TEXT),
                null=True,
            ),
        ),
    ]