# Generated by Django 5.2.3 on 2025-06-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('RM', 'Remote'), ('CT', 'Contract'), ('IN', 'Internship')], default=None, max_length=2),
            preserve_default=False,
        ),
    ]
