# Generated by Django 3.2.8 on 2022-07-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20220708_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maker',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='packing',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='originalpacking',
            unique_together={('packing', 'quantity', 'unit')},
        ),
    ]
