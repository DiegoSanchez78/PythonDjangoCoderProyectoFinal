# Generated by Django 5.0.1 on 2024-03-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_curso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='detalle',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/'),
        ),
    ]
