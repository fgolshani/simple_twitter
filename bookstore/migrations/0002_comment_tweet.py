# Generated by Django 2.0.4 on 2018-04-08 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Tweet'),
            preserve_default=False,
        ),
    ]
