# Generated by Django 4.0.4 on 2022-07-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0010_merge_20220630_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerveza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
