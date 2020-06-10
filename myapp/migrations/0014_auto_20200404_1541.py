# Generated by Django 3.0.4 on 2020-04-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='id',
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='example', help_text='Slug for blog.', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='example', help_text='Blog tag.', max_length=50),
            preserve_default=False,
        ),
    ]