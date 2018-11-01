# Generated by Django 2.1.2 on 2018-10-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ej_conversations', '0002_change_meta_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='hidden',
            field=models.BooleanField(default=False, help_text="Hidden conversations doesn't appears in his board", verbose_name='hidden'),
        ),
    ]
