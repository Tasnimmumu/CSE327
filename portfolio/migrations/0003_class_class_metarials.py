# Generated by Django 3.2.5 on 2021-07-05 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210704_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(default=None, max_length=30)),
                ('section', models.IntegerField(default=None)),
                ('Invitation_Code', models.CharField(default=None, max_length=6)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.student')),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Class_Metarials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(default=None)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('Submit_Date', models.DateField(default=None)),
                ('Pdf', models.FileField(upload_to='')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.class')),
            ],
        ),
    ]
