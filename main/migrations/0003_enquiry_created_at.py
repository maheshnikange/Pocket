# Generated by Django 5.0.4 on 2024-05-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_enquiry_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]