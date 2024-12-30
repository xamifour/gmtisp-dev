# Generated by Django 3.1.13 on 2021-12-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gmtisp_radius', '0023_registereduser_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationradiussettings',
            name='sms_verification',
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text=(
                    'Whether users who sign up should be required to '
                    'verify their mobile phone number via SMS'
                ),
                null=True,
            ),
        ),
    ]
