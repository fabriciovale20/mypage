# Generated by Django 3.2.5 on 2021-07-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcmapp', '0007_auto_20210710_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
