# Generated by Django 4.0.4 on 2022-04-27 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spotted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(choices=[('N', 'North America'), ('S', 'South America'), ('A', 'Africa'), ('E', 'Europe'), ('S', 'Asia'), ('U', 'Australia'), ('T', 'Antarctica')], default='N', max_length=1)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
        ),
    ]