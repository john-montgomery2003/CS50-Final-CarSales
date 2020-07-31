# Generated by Django 3.0.8 on 2020-07-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('milage', models.IntegerField()),
                ('emissions', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('new', models.BooleanField()),
                ('sold', models.BooleanField()),
                ('soldDate', models.DateField(blank=True, null=True)),
                ('postDate', models.DateField()),
                ('Main_Image', models.ImageField(default='media/default.jpg', upload_to='')),
                ('Side_Image', models.ImageField(default='media/default.jpg', upload_to='')),
                ('Back_Image', models.ImageField(default='media/default.jpg', upload_to='')),
                ('Front_Image', models.ImageField(default='media/default.jpg', upload_to='')),
                ('Interior_Image', models.ImageField(default='media/default.jpg', upload_to='')),
                ('Other_Image', models.ImageField(default='media/default.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.CharField(max_length=255)),
                ('responded', models.BooleanField(default=False)),
            ],
        ),
    ]
