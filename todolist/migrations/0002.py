from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='added_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolist',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]