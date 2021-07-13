# Generated by Django 3.2.5 on 2021-07-13 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tcmapp', '0013_auto_20210712_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='cadastro',
            old_name='observacoes',
            new_name='informacoes',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='situacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tcmapp.situacao'),
        ),
    ]
