# Generated by Django 2.2.3 on 2019-08-12 15:32

from django.db import migrations, models
import django.db.models.deletion
from django.apps import apps


class Migration(migrations.Migration):

    def create_default_resolution(apps, schema_editor):
        Resolution = apps.get_model("common", "Resolution")
        defaultresolution = Resolution(resolution="No resolution recorded")
        defaultresolution.save()

    dependencies = [
        ('common', '0002_auto_20190730_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.TextField(unique=True)),
            ],
        ),

        migrations.RunPython(create_default_resolution),
        
        migrations.AddField(
            model_name='crime',
            name='resolution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='common.Resolution'),
        ),
    ]
