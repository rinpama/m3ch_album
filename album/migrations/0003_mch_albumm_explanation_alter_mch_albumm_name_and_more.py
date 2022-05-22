# Generated by Django 4.0.3 on 2022-03-27 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_rename_mch_album_mch_albumm'),
    ]

    operations = [
        migrations.AddField(
            model_name='mch_albumm',
            name='explanation',
            field=models.TextField(default='---', verbose_name='情報'),
        ),
        migrations.AlterField(
            model_name='mch_albumm',
            name='name',
            field=models.CharField(max_length=20, verbose_name='なまえ'),
        ),
        migrations.AlterField(
            model_name='mch_albumm',
            name='title',
            field=models.CharField(max_length=50, verbose_name='タイトル'),
        ),
    ]
