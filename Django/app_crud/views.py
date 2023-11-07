from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import schoolserializer
from .serializers import studentserializer
from .serializers import teacherserializer
from .serializers import courseserializer
from .serializers import busserializer
from .serializers import Facultyserializer
from .models import *
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, "demo.html")


@api_view(['GET'])
def School(request, sn, sa, snum, se):
    school.objects.create(
        school_name=sn,
        school_address=sa,
        school_number=snum,
        school_email=se
    )
    all_school = school.objects.all()
    serial = schoolserializer(all_school, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_School(request):
    all_school = school.objects.all()
    serial = schoolserializer(all_school, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_School(request, pk):
    del_school = get_object_or_404(school, id=pk)
    del_school.delete()
    serial = schoolserializer(del_school)
    return Response(serial.data)


@api_view(['GET'])
def up_School(request, pk, sn, sa, snum, se):
    up_school = get_object_or_404(school, id=pk)
    up_school.school_name = sn
    up_school.school_address = sa
    up_school.school_number = snum
    up_school.school_email = se
    up_school.save()
    serial = schoolserializer(up_school)
    return Response(serial.data)


@api_view(['GET'])
def add_student(request, sn, ssn, ss, sa, aa, sc, sf):
    find1 = school.objects.filter(school_name=ssn).first()
    find = teacher.objects.filter(Q(class_teacher=ss) & Q(school_t_name=ssn)).first()
    find2 = bus.objects.filter(bus_root=aa).first()

    student.objects.create(
        student_name=sn,
        student_school_name=ssn,
        student_std=ss,
        student_address=sa,
        student_a_area=aa,
        student_course=sc,
        student_fees=sf,
        sch=find1,
        tch=find,
        Bus=find2
    )
    all_student = student.objects.all()
    serial = studentserializer(all_student, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_student(reqeust):
    All_student = student.objects.all()
    serial = studentserializer(All_student, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_student(request, pk):
    Del_student = get_object_or_404(student, id=pk)
    Del_student.delete()
    serial = studentserializer(Del_student)
    return Response(serial.data)


@api_view(['GET'])
def up_student(request, pk, sn, ssn, ss, sa, aa, sc, sf):
    up_Student = get_object_or_404(student, id=pk)
    up_Student.student_name = sn
    up_Student.student_school_name = ssn
    up_Student.student_std = ss
    up_Student.student_address = sa
    up_Student.student_a_area = aa
    up_Student.student_course = sc
    up_Student.student_fees = sf
    up_Student.save()
    serial = studentserializer(up_Student)
    return Response(serial.data)


@api_view(['GET'])
def add_teacher(requrst, tn, stn, ct, ts):
    find = school.objects.filter(school_name=stn).first()

    teacher.objects.create(
        teacher_name=tn,
        school_t_name=stn,
        class_teacher=ct,
        teacher_salary=ts,
        sch=find
    )
    all_teacher = teacher.objects.all()
    serial = teacherserializer(all_teacher, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_teacher(request):
    All_teacher = teacher.objects.all()
    serial = teacherserializer(All_teacher, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_teacher(request, pk):
    Del_teacher = get_object_or_404(teacher, id=pk)
    Del_teacher.delete()
    serial = teacherserializer(Del_teacher)
    return Response(serial.data)


@api_view(['GET'])
def up_teacher(request, pk, tn, stn, ct, ts):
    up_Teacher = get_object_or_404(teacher, id=pk)
    up_Teacher.teacher_name = tn
    up_Teacher.school_t_name = stn
    up_Teacher.class_teacher = ct
    up_Teacher.teacher_salary = ts
    up_Teacher.save()
    serial = teacherserializer(up_Teacher)
    return Response(serial.data)


# @api_view(['GET'])
# def add_clark(request, cn, cp, cs):
#     find = school.objects.filter(school_name=cs).first()
#     clark.objects.create(
#         clark_name=cn,
#         clark_position=cp,
#         clark_school=cs,
#         sch=find
#     )
#     all_clark = clark.objects.all()
#     serial = clarkserializer(all_clark, many=True)
#     return Response(serial.data)
#
#
# @api_view(['GET'])
# def all_clark(request):
#     All_clark = clark.objects.all()
#     serial = clarkserializer(All_clark, many=True)
#     return Response(serial.data)
#
#
# @api_view(['GET'])
# def del_clark(request, pk):
#     one_delete = get_object_or_404(clark, id=pk)
#     one_delete.delete()
#     serializer = clarkserializer(one_delete)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def up_clark(request, pk, cn, cp, cs):
#     one_update = get_object_or_404(clark, id=pk)
#     one_update.clark_name = cn
#     one_update.clark_position = cp
#     one_update.clark_school = cs
#     one_update.save()
#     serial = clarkserializer(one_update)
#     return Response(serial.data)


@api_view(['GET'])
def add_course(request, c, f):
    find = student.objects.filter(student_course=c).first()
    course.objects.create(
        course_name=c,
        course_fees=f,
        stu=find
    )
    all_course = course.objects.all()
    serial = courseserializer(all_course, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_course(request):
    All_course = course.objects.all()
    serial = courseserializer(All_course, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_course(request, pk):
    Del_course = get_object_or_404(course, id=pk)
    Del_course.delete()
    serial = courseserializer(Del_course)
    return Response(serial.data)


@api_view(['GET'])
def up_course(request, pk, c, f):
    one_course = get_object_or_404(course, id=pk)
    one_course.course_name = c
    one_course.course_fees = f
    serial = courseserializer(one_course)
    return Response(serial.data)


@api_view(['GET'])
def view_course(request, c):
    students = student.objects.filter(student_course=c)
    serializer = studentserializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def add_bus(request, dn, br, sb):
    bus.objects.create(
        driver_name=dn,
        bus_root=br,
        school_bus=sb,
    )
    Bus = bus.objects.all()
    serial = busserializer(Bus, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_bus(request):
    Bus = bus.objects.all()
    serial = busserializer(Bus, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_bus(request, pk):
    Del_bus = get_object_or_404(bus, id=pk)
    Del_bus.delete()
    serial = busserializer(Del_bus)
    return Response(serial.data)


@api_view(['GET'])
def up_bus(request, pk, dn, br, sb):
    Up_bus = get_object_or_404(bus, id=pk)
    Up_bus.driver_name = dn
    Up_bus.bus_root = br
    Up_bus.school_bus = sb
    serial = busserializer(Up_bus)
    return Response(serial.data)


@api_view(['GET'])
def view_area(request, aa):
    students = student.objects.filter(student_a_area=aa)
    serializer = studentserializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def add_faculty(request, fn, fp, fs, sof):
    find = school.objects.filter(school_name=sof).first()
    Faculty.objects.create(
        faculty_name=fn,
        faculty_position=fp,
        faculty_salary=fs,
        school_of_faculty=sof,
        sch=find
    )
    All_faculty = Faculty.objects.all()
    serial = Facultyserializer(All_faculty, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_faculty(request):
    all_f = Faculty.objects.all()
    serial = Facultyserializer(all_f, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_faculty(request, pk):
    Del_faculty = get_object_or_404(Faculty, id=pk)
    Del_faculty.delete()
    serial = Facultyserializer(Del_faculty)
    return Response(serial.data)


@api_view(['GET'])
def up_faculty(request, pk, fn, fp, fs, sof):
    Up_faculty = get_object_or_404(Faculty, id=pk)
    Up_faculty.faculty_name = fn
    Up_faculty.faculty_position = fp
    Up_faculty.faculty_salary = fs
    Up_faculty.school_of_faculty = sof
    serial = Facultyserializer(Up_faculty)
    return Response(serial.data)


@api_view(['GET'])
def view_faculty(request,vf):
    if vf == 'teacher' or vf == 'Teacher':
        pass

    else:
