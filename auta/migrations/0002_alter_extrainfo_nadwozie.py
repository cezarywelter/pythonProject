# Generated by Django 4.2.1 on 2023-06-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='nadwozie',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'combi'), (4, 'kabriolet'), (5, 'coupe'), (6, 'roadster'), (3, 'sedan'), (0, 'pick-up'), (1, 'Hatchback')], null=True),
        ),
    ]
