# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    semester = models.ForeignKey('Semester', models.DO_NOTHING, db_column='Semester', blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cat_num = models.CharField(db_column='Cat_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    credit_hours = models.DecimalField(db_column='Credit_Hours', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'class'


class Mode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mode'


class PrefType(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='Type_Name', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pref_type'


class ProfPreferences(models.Model):
    profid = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ProfID')  # Field name made lowercase.
    pref_type = models.ForeignKey(PrefType, models.DO_NOTHING, db_column='Pref_Type')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.
    scalar = models.IntegerField(db_column='Scalar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prof_preferences'


class ProfSpouse(models.Model):
    id1 = models.OneToOneField('Professor', models.DO_NOTHING, db_column='Id1', primary_key=True)  # Field name made lowercase.
    id2 = models.ForeignKey('Professor', models.DO_NOTHING, db_column='Id2', related_name='+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prof_spouse'
        unique_together = (('id1', 'id2'),)


class ProfType(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=45)
    class_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prof_type'


class Professor(models.Model):
    fname = models.CharField(db_column='FName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=15)  # Field name made lowercase.
    prof_type = models.ForeignKey(ProfType, models.DO_NOTHING, db_column='Prof_Type', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.CharField(db_column='Internal_ID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'


class Room(models.Model):
    building = models.CharField(db_column='Building', max_length=15)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=10)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Section(models.Model):
    section = models.IntegerField(db_column='Section', primary_key=True)  # Field name made lowercase.
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='Class')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    type = models.CharField(db_column='Type', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mode = models.ForeignKey(Mode, models.DO_NOTHING, db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    prof = models.ForeignKey(Professor, models.DO_NOTHING, db_column='Prof_id', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    end = models.DateTimeField(db_column='End', blank=True, null=True)  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=7, blank=True, null=True)  # Field name made lowercase.
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='Room_id', blank=True, null=True)  # Field name made lowercase.
    seats = models.IntegerField(db_column='Seats', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('section', 'class_field'),)


class Semester(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    semester_type = models.ForeignKey('SemesterType', models.DO_NOTHING, db_column='Semester_Type', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'semester'


class SemesterType(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semester_type'
