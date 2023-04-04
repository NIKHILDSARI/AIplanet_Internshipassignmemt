# Generated by Django 4.1.7 on 2023-04-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackathon_api', '0005_submissions_submission_as_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submission_as_file',
            field=models.FileField(blank=True, default='empty', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='submission_as_link',
            field=models.URLField(blank=True, default='empty'),
        ),
    ]
