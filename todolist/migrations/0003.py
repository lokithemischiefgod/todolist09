from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='added_time',
        ),
    ]