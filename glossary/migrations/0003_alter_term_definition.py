# Generated by Django 5.0 on 2023-12-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_alter_term_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='definition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
