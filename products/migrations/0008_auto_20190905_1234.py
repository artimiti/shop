# Generated by Django 2.2.4 on 2019-09-05 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190905_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='category',
        ),
    ]
