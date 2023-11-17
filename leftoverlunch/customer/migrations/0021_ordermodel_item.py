# Generated by Django 4.2.5 on 2023-10-14 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_ordermodel_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='item',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='customer.menuitem'),
        ),
    ]
