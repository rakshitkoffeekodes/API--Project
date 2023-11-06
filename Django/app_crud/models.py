from django.db import models


# Create your models here.

class school(models.Model):
    school_name = models.CharField(max_length=500)
    school_address = models.CharField(max_length=1000)
    school_number = models.IntegerField(default=0)
    school_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.school_name


class teacher(models.Model):
    teacher_name = models.CharField(max_length=500)
    school_t_name = models.CharField(max_length=500)
    class_teacher = models.CharField(max_length=50)
    teacher_salary = models.IntegerField(default=0)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class bus(models.Model):
    driver_name = models.CharField(max_length=500)
    bus_root = models.CharField(max_length=500)
    school_bus = models.CharField(max_length=500)

    def __str__(self):
        return self.driver_name


class student(models.Model):
    student_name = models.CharField(max_length=500)
    student_school_name = models.CharField(max_length=500)
    student_std = models.CharField(max_length=50)
    student_address = models.CharField(max_length=1000, null=True)
    student_a_area = models.CharField(max_length=200, null=True)
    student_course = models.CharField(max_length=500, null=True)
    student_fees = models.IntegerField(default=0)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)
    tch = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
    Bus = models.ForeignKey(bus, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.student_name


class clark(models.Model):
    clark_name = models.CharField(max_length=500)
    clark_position = models.CharField(max_length=500)
    clark_school = models.CharField(max_length=500)
    sch = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return self.clark_name


class course(models.Model):
    course_name = models.CharField(max_length=500)
    course_fees = models.IntegerField()
    stu = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class salary(models.Model):
    teacher_salary = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=500)
    tech = models.ForeignKey(teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name + self.teacher_salary
