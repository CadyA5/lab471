
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0001_initial'),
    ]

    operations = [
  migrations.CreateModel(
  name='Address',
  fields=[
     ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmodule.address')),
            ],
        ),
    ]
