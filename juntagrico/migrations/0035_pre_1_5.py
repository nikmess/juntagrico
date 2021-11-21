# Generated by Django 3.2 on 2021-11-16 07:59

from django.db import migrations
import juntagrico.entity


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico', '0034_auto_20210415_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=juntagrico.entity.LowercaseEmailField(max_length=254, unique=True),
        ),
    ]
