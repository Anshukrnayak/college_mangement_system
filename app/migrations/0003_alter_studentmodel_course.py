# Generated by Django 5.1.6 on 2025-02-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_coursemodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='course',
            field=models.ManyToManyField(related_name='student', to='app.coursemodel'),
        ),
    ]
