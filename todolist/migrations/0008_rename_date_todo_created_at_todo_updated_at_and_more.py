# Generated by Django 5.1.3 on 2024-12-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_todo_delete_todolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]