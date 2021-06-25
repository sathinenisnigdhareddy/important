# Generated by Django 3.2.1 on 2021-06-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lecture_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_topic', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('lecture_vedios', models.FileField(null=True, upload_to='tutorial/attachments/')),
                ('lecture_notes', models.FileField(null=True, upload_to='tutorial/notes/')),
            ],
        ),
    ]