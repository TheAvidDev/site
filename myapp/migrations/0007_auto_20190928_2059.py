# Generated by Django 2.2.5 on 2019-09-29 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190928_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]