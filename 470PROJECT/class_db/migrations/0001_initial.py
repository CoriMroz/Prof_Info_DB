# Generated by Django 3.1.7 on 2021-05-03 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(blank=True, db_column='Program', max_length=10, null=True)),
                ('cat_num', models.CharField(blank=True, db_column='Cat_Num', max_length=10, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('credit_hours', models.DecimalField(blank=True, db_column='Credit_Hours', decimal_places=0, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'mode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrefType',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, db_column='Type_Name', max_length=45, null=True, unique=True)),
            ],
            options={
                'db_table': 'pref_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, db_column='FName', max_length=15, null=True)),
                ('lname', models.CharField(db_column='LName', max_length=15)),
                ('internal_id', models.CharField(blank=True, db_column='Internal_ID', max_length=45, null=True, unique=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(db_column='Start')),
                ('end', models.DateTimeField(db_column='End')),
                ('scalar', models.IntegerField(blank=True, db_column='Scalar', null=True)),
            ],
            options={
                'db_table': 'prof_preferences',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=45, unique=True)),
                ('class_hours', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prof_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(db_column='Building', max_length=15)),
                ('number', models.CharField(db_column='Number', max_length=10)),
                ('capacity', models.IntegerField(blank=True, db_column='Capacity', null=True)),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section', models.IntegerField(db_column='Section', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=5, null=True)),
                ('start', models.DateTimeField(blank=True, db_column='Start', null=True)),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('days', models.CharField(blank=True, db_column='Days', max_length=7, null=True)),
                ('seats', models.IntegerField(blank=True, db_column='Seats', null=True)),
            ],
            options={
                'db_table': 'section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('year', models.TextField(db_column='Year')),
            ],
            options={
                'db_table': 'semester',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SemesterType',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('type', models.CharField(db_column='Type', max_length=15)),
            ],
            options={
                'db_table': 'semester_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfSpouse',
            fields=[
                ('id1', models.OneToOneField(db_column='Id1', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='class_db.professor')),
            ],
            options={
                'db_table': 'prof_spouse',
                'managed': False,
            },
        ),
    ]