# Generated by Django 3.2.6 on 2023-04-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='Document_Attach',
            field=models.ImageField(blank=True, null=True, upload_to='DocumentAttach/'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Primary_Mail',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]