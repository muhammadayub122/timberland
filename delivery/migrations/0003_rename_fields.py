# Generated migration to fix foreign key constraint issue

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_deliveryaddress_options_alter_delivery_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverygroup',
            name='message_id',
        ),
        migrations.RemoveField(
            model_name='deliverygroup',
            name='topic_id',
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='message_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='topic_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
