# Generated by Django 3.1.7 on 2021-04-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20210330_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال این درخواست'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='خوانده شده/خوانده نشده'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='شماره شما چیست؟'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(verbose_name='توضیحات خود را وارد نمایید'),
        ),
    ]