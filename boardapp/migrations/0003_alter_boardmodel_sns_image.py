# Generated by Django 5.0.7 on 2024-08-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_alter_boardmodel_good_alter_boardmodel_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='sns_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
