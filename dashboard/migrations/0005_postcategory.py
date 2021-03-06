# Generated by Django 3.0.3 on 2020-03-16 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200316_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Category')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Post')),
            ],
        ),
    ]
