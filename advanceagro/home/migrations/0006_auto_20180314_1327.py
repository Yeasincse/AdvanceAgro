# Generated by Django 2.0.3 on 2018-03-14 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180314_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmdschedule',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FMD', to='home.DiseaseManagement', verbose_name='গরু নং'),
        ),
    ]
