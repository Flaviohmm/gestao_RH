# Generated by Django 3.2.9 on 2021-11-12 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0002_auto_20211110_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]