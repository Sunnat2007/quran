# Generated by Django 4.0.4 on 2022-04-30 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quronuz', '0009_sura_delete_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='oyat',
            name='sura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quronuz.sura'),
        ),
    ]