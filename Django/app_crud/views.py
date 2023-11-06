from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import schoolserializer
from .serializers import studentserializer
from .serializers import teacherserializer
from .serializers import clarkserializer
from .models import *
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, "demo.html")


@api_view(['GET'])
def School(request, n, a, c, s, co):
    school.objects.create(
        school_name=n,
        school_address=a,
        school_city=c,
        school_state=s,
        school_Country=co
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
def up_School(request, pk, n, a, c, s, co):
    up_school = get_object_or_404(school, id=pk)
    up_school.school_name = n
    up_school.school_address = a
    up_school.school_city = c
    up_school.school_state = s
    up_school.school_contry = co
    up_school.save()
    serial = schoolserializer(up_school)
    return Response(serial.data)


@api_view(['GET'])
def add_student(request, sn, ssn, ss):
    find1 = school.objects.filter(school_name=ssn).first()
    find = teacher.objects.filter(Q(class_teacher=ss) & Q(school_t_name=ssn)).first()

    student.objects.create(
        student_name=sn,
        student_school_name=ssn,
        student_std=ss,
        sch=find1,
        tch=find
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
def up_student(request, pk, sn, ssn, ss):
    up_Student = get_object_or_404(student, id=pk)
    up_Student.student_name = sn
    up_Student.student_school_name = ssn
    up_Student.student_std = ss
    up_Student.save()
    serial = studentserializer(up_Student)
    return Response(serial.data)


@api_view(['GET'])
def add_teacher(requrst, tn, stn, ct):
    find = school.objects.filter(school_name=stn).first()

    teacher.objects.create(
        teacher_name=tn,
        school_t_name=stn,
        class_teacher=ct,
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
def up_teacher(request, pk, tn, stn, ct):
    up_Teacher = get_object_or_404(teacher, id=pk)
    up_Teacher.teacher_name = tn
    up_Teacher.school_t_name = stn
    up_Teacher.class_teacher = ct
    up_Teacher.save()
    serial = teacherserializer(up_Teacher)
    return Response(serial.data)


@api_view(['GET'])
def add_clark(request, cn, cp, cs):
    find = school.objects.filter(school_name=cs).first()
    clark.objects.create(
        clark_name=cn,
        clark_position=cp,
        clark_school=cs,
        sch=find
    )
    all_clark = clark.objects.all()
    serial = clarkserializer(all_clark, many=True)
    return Response(serial.data)


@api_view(['GET'])
def all_clark(request):
    All_clark = clark.objects.all()
    serial = clarkserializer(All_clark, many=True)
    return Response(serial.data)


@api_view(['GET'])
def del_clark(request, pk):
    one_delete = get_object_or_404(clark, id=pk)
    one_delete.delete()
    serializer = clarkserializer(one_delete)
    return Response(serializer.data)


@api_view(['GET'])
def up_clark(request, pk, cn, cp, cs):
    one_update = get_object_or_404(clark, id=pk)
    one_update.clark_name = cn
    one_update.clark_position = cp
    one_update.clark_school = cs
    one_update.save()
    serial = clarkserializer(one_update)
    return Response(serial.data)
