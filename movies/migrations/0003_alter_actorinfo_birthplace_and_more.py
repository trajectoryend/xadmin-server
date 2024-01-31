# Generated by Django 4.2.9 on 2024-01-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorinfo',
            name='birthplace',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='出生地'),
        ),
        migrations.AlterField(
            model_name='actorinfo',
            name='foreign_name',
            field=models.CharField(max_length=256, verbose_name='外文'),
        ),
        migrations.AlterField(
            model_name='actorinfo',
            name='name',
            field=models.CharField(max_length=256, verbose_name='演员名字'),
        ),
        migrations.AlterField(
            model_name='actorinfo',
            name='profession',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='episodeinfo',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='电影单集名称'),
        ),
        migrations.AlterField(
            model_name='filminfo',
            name='name',
            field=models.CharField(max_length=256, verbose_name='电影片名'),
        ),
        migrations.AlterField(
            model_name='swipeinfo',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='轮播名称'),
        ),
        migrations.AlterField(
            model_name='swipeinfo',
            name='route',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='前端路由地址'),
        ),
    ]
