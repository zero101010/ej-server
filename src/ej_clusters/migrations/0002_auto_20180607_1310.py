# Generated by Django 2.0.5 on 2018-06-07 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ej_clusters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stereotypeclustermap',
            name='conversation',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='ej_conversations.Conversation'),
        ),
    ]