# Generated by Django 4.0.3 on 2022-04-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.CharField(max_length=20, verbose_name='Автор'),
        ),
    ]
