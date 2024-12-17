from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.CharField(max_length=50),
        ),
    ]