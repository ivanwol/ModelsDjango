# Generated by Django 4.0.5 on 2022-07-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_person_delete_typefields'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
