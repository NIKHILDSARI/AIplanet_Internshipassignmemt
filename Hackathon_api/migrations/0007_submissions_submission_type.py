# Generated by Django 4.1.7 on 2023-04-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackathon_api', '0006_alter_submissions_submission_as_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='submission_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
