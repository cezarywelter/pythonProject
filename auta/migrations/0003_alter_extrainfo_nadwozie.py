# Generated by Django 4.2.1 on 2023-06-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auta', '0002_alter_extrainfo_nadwozie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='nadwozie',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'sedan'), (4, 'kabriolet'), (1, 'Hatchback'), (0, 'pick-up'), (2, 'combi'), (6, 'roadster'), (5, 'coupe')], null=True),
        ),
    ]
