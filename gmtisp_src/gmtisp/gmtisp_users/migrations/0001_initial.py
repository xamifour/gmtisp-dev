# Generated by Django 3.1.8 on 2021-11-27 15:27

import uuid

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import organizations.base
import organizations.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models

import openwisp_users.base.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text=(
                            'Designates that this user has all permissions '
                            'without explicitly assigning them.'
                        ),
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={
                            'unique': 'A user with that username already exists.'
                        },
                        help_text=(
                            'Required. 150 characters or fewer. '
                            'Letters, digits and @/./+/-/_ only.'
                        ),
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name='username',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='last name'
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text=(
                            'Designates whether the user can log into this admin site.'
                        ),
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text=(
                            'Designates whether this user should be '
                            'treated as active. Unselect this instead '
                            'of deleting accounts.'
                        ),
                        verbose_name='active',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='date joined'
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name='email address',
                    ),
                ),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                (
                    'company',
                    models.CharField(blank=True, max_length=30, verbose_name='company'),
                ),
                (
                    'location',
                    models.CharField(
                        blank=True, max_length=256, verbose_name='location'
                    ),
                ),
                (
                    'phone_number',
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        unique=True,
                        verbose_name='phone number',
                    ),
                ),
                (
                    'social_security_number',
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                '^\\d\\d\\d-\\d\\d-\\d\\d\\d\\d$'
                            )
                        ],
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text=(
                            'The groups this user belongs to. A user will get '
                            'all permissions granted to each of their groups.'
                        ),
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.Permission',
                        verbose_name='user permissions',
                    ),
                ),
                (
                    'birth_date',
                    models.DateField(blank=True, null=True, verbose_name='birth date'),
                ),
                (
                    'language',
                    models.CharField(
                        choices=settings.LANGUAGES,
                        default=settings.LANGUAGE_CODE,
                        max_length=8,
                    ),
                ),
                (
                    'password_updated',
                    models.DateField(
                        blank=True, null=True, verbose_name="password updated"
                    ),
                ),
                (
                    'notes',
                    models.TextField(
                        blank=True,
                        help_text='notes for internal usage',
                        verbose_name='notes',
                    ),
                ),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'index_together': {('id', 'email')},
            },
            managers=[
                ('objects', openwisp_users.base.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                (
                    'name',
                    models.CharField(
                        help_text='The name of the organization', max_length=200
                    ),
                ),
                ('is_active', models.BooleanField(default=True)),
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'slug',
                    organizations.fields.SlugField(
                        blank=True,
                        editable=False,
                        help_text=(
                            'The name in all lowercase, suitable for '
                            'URL identification'
                        ),
                        max_length=200,
                        populate_from='name',
                        unique=True,
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'description',
                    models.TextField(blank=True, verbose_name='description'),
                ),
                (
                    'email',
                    models.EmailField(blank=True, max_length=254, verbose_name='email'),
                ),
                ('url', models.URLField(blank=True, verbose_name='URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=(openwisp_users.base.models.BaseGroup, 'auth.group'),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ('is_admin', models.BooleanField(default=False)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='organization_users',
                        to='gmtisp_users.organization',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='gmtisp_users_organizationuser',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'abstract': False,
                'ordering': ['organization', 'user'],
                'verbose_name': 'organization user',
                'verbose_name_plural': 'organization users',
                'unique_together': {('user', 'organization')},
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(
                related_name='gmtisp_users_organization',
                through='gmtisp_users.OrganizationUser',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={
                'ordering': ['name'],
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='OrganizationOwner',
            fields=[
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'organization',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='owner',
                        to='gmtisp_users.organization',
                    ),
                ),
                (
                    'organization_user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='gmtisp_users.organizationuser',
                    ),
                ),
            ],
            options={
                'abstract': False,
                'verbose_name': 'organization owner',
                'verbose_name_plural': 'organization owners',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(
                choices=settings.LANGUAGES,
                default=settings.LANGUAGE_CODE,
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(
                related_name='%(app_label)s_%(class)s',
                through='gmtisp_users.OrganizationUser',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='organizationuser',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='%(app_label)s_%(class)s',
                to='gmtisp_users.user',
            ),
        ),
        migrations.CreateModel(
            name='OrganizationInvitation',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('guid', models.UUIDField(editable=False)),
                (
                    'invitee_identifier',
                    models.CharField(
                        help_text=(
                            'The contact identifier for the invitee,'
                            ' email, phone number, social media handle, etc.'
                        ),
                        max_length=1000,
                    ),
                ),
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'invited_by',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='%(app_label)s_%(class)s_sent_invitations',
                        to='gmtisp_users.user',
                    ),
                ),
                (
                    'invitee',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='%(app_label)s_%(class)s_invitations',
                        to='gmtisp_users.user',
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='organization_invites',
                        to='gmtisp_users.organization',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
