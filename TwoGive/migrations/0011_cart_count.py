# Generated by Django 2.2.6 on 2019-11-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwoGive', '0010_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]