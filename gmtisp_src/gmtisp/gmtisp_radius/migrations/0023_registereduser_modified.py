# Generated by Django 3.1.8 on 2021-11-09 12:14

import django.utils.timezone
import model_utils.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gmtisp_radius', '0022_registered_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name='Last verification change',
            ),
        ),
    ]
