# Generated by Django 3.2.5 on 2021-07-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcmapp', '0010_auto_20210712_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
