from django.db import models


# Create your models here.

class school(models.Model):
    school_name = models.CharField(max_length=500)
    school_address = models.CharField(max_length=1000)
    school_city = models.CharField(max_length=200)
    school_state = models.CharField(max_length=200)
    school_Country = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name

class teacher(models.Model):
    teacher_name = models.CharField(max_length=500)
    school_t_name = models.CharField(max_length=500)
    class_teacher = models.CharField(max_length=50)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name

class student(models.Model):
    student_name = models.CharField(max_length=500)
    student_school_name = models.CharField(max_length=500)
    student_std = models.CharField(max_length=50)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)
    tch = models.ForeignKey(teacher,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.student_name

class clark(models.Model):
    clark_name = models.CharField(max_length=500)
    clark_position = models.CharField(max_length=500)
    clark_school = models.CharField(max_length=500)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return self.clark_name