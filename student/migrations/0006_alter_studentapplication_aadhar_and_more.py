# Generated by Django 4.1 on 2023-05-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_studentapplication_relationship_of_guardian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='Aadhar',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='higher_secondary_certificate_upload',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentapplication',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
