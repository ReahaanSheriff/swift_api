# Generated by Django 3.0.6 on 2021-11-10 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shippingdjango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createshipment',
            old_name='user_id',
            new_name='user_id_id',
        ),
    ]