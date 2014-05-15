from django.db import models
from django.db.models import Avg

class Semester(models.Model):
    begin = models.DateField()
    end = models.DateField()
    def __unicode__(self):
        return u"{0} - {1}".format(self.begin, self.end)

class Year(models.Model):
    name = models.CharField(max_length=255)
    semester_1 = models.OneToOneField(Semester, related_name="semester_1")
    semester_2 = models.OneToOneField(Semester, related_name="semester_2")
    marks_interval_min = models.IntegerField()
    marks_interval_max = models.IntegerField()
    def __unicode__(self):
        return u"{0}".format(self.name)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255, blank= True)
    year = models.ForeignKey(Year)
    typs = models.ManyToManyField("Typ", blank= False)
    def __unicode__(self):
        return u"{0}".format(self.name)
    def get_typs(self):
        typs = self.typs.all().values_list("name", flat=True)
        return ", ".join(typs)
    get_typs.short_description = "Typs"
    def get_avg(self):
        average = Decimal("0.00")
        Mark.objects.all().aggregate(Avg('value'))
        return average.quantize(Decimal("0.00"))



class Typ(models.Model):
    name = models.CharField(max_length=255)
    valence = models.FloatField()
    def __unicode__(self):
        return u"{0} ({1}%)".format(self.name, self.valence)

class Mark(models.Model):
    value = models.IntegerField()
    date = models.DateField()
    topic = models.CharField(max_length=255, blank= True)
    typ = models.ForeignKey(Typ)
    semester = models.ForeignKey(Semester)
    subject = models.ForeignKey(Subject)
    def __unicode__(self):
        return u"{0}".format(self.topic)
