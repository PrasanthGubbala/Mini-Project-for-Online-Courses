from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Admin,CourseInfo,StudentInfo,EnrolledCourses
from django.db.utils import IntegrityError
#admin panel
def admin(request):
    return render(request, 'admin/admin_login.html')

def check_admin(request):
    uname = request.POST.get('un')
    password = request.POST.get('pw')
    try:
        admin = Admin.objects.get(user_name=uname)
        if uname == admin.user_name and password == admin.password:
            return render(request, 'admin/admin_home.html', {'admin':admin})
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('admin')
    except Admin.DoesNotExist:
        messages.error(request, "User does't exist")
        return redirect('admin')

def admin_home(request):
    uname = request.GET.get('uname')
    admin = Admin.objects.get(user_name=uname)
    return render(request, "admin/admin_home.html", {'admin':admin})

def schedule_new_class(request):
    #uname = request.GET.get('uname')
    un = Admin.objects.get(user_name='sathya tech')
    return render(request, 'admin/schedule_new_class.html',{'admin':un})

def save_course(request):
    course = request.POST.get('course')
    tutor = request.POST.get('tutor')
    date = request.POST.get('date')
    time = request.POST.get('time')
    fee = request.POST.get('fee')
    duration = request.POST.get('duration')
    try:
        CourseInfo(course_name=course,tutor=tutor,start_date=date,class_time=time,fee=fee,duration=duration).save()
        messages.success(request,'Class is Scheduled')
        return redirect('view_all_courses')
    except IntegrityError:
        messages.error(request,'your given data is already exist')
        return redirect('schedule_new_class')

def view_all_courses(request):
    un = Admin.objects.get(user_name='sathya tech')
    qs = CourseInfo.objects.all()
    return render(request, 'admin/view_all_courses.html', {'data':qs, 'admin':un})

def delete_course(request):
    cid = request.GET.get('cid')
    try:
        CourseInfo.objects.get(course_id=cid).delete()
        return redirect('view_all_courses')
    except CourseInfo.DoesNotExist:
        return redirect('view_all_courses')

def update_course(request):
    cid = request.GET.get('cid')
    course = CourseInfo.objects.get(course_id=cid)
    un = Admin.objects.get(user_name='sathya tech')
    return render(request, 'admin/update_course.html', {'course':course,'admin':un})

def update_course_save(request):
    cid = request.POST.get('id')

    course = request.POST.get('course')
    tutor = request.POST.get('tutor')
    date = request.POST.get('date')
    time = request.POST.get('time')
    fee = request.POST.get('fee')
    duration = request.POST.get('duration')

    CourseInfo.objects.filter(course_id=cid).update(course_name=course,tutor=tutor,start_date=date,class_time=time,fee=fee,duration=duration)
    messages.success(request,'data updated successfully')
    return redirect('view_all_courses')

#student panel
def student_main(request):
    courses = CourseInfo.objects.all()
    return render(request, 'student/student_main.html', {'courses':courses})

def student_register(request):
    return render(request, 'student/student_register.html')

def save_student_registration(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if password == password2:
        try:
            StudentInfo(name=name,contact=contact,email=email,password=password).save()
            messages.success(request,'Information is saved into db! now you can login into your account')
            return redirect('student_login')

        except IntegrityError as ie:
            messages.error(request,ie)
            return redirect('student_register')

    else:
        messages.error(request,"Entered Password In Both Fields Are Did't Match")
        return redirect('student_register')

def student_login(request):
    return render(request, 'student/student_login.html')

def student_login_check(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        student = StudentInfo.objects.get(email=email)
        if email == student.email and password == student.password:
            return render(request,'student/student_home.html',{'student':student})
        else:
            messages.error(request,'email or password are incorrect')
            return redirect('student_login')
    except StudentInfo.DoesNotExist as de:
        messages.error(request,de)
        return redirect('student_login')

def contact_us(request):
    admin = Admin.objects.all()
    return render(request, 'student/contact_us.html',{'admin':admin[0]})

def student_home_cont(request):
    email = request.GET.get('email')
    student = StudentInfo.objects.get(email=email)
    return render(request, 'student/student_home_cont.html', {'student':student})

def enroll_the_course(request):
    email = request.GET.get('email')
    try:
        student = StudentInfo.objects.get(email=email)
        qs = CourseInfo.objects.all()
        return render(request, 'student/enroll_the_course.html', {'student':student,'data':qs})
    except StudentInfo.DoesNotExist as de:
        messages.success(request, de)
        return redirect('enroll_the_course')

def enroll_course(request):
    cid = request.GET.get('cid')
    email = request.GET.get('email')
    try:
        student = StudentInfo.objects.get(email=email)
        EnrolledCourses(course_id=cid,email=email).save()
        messages.success(request,'Enrolled')
        return redirect('view_all_enrolled_classes')

    except IntegrityError as ie:
        messages.error(request,ie)
        return redirect('enroll_the_course')

def view_all_enrolled_classes(request):
    email = request.GET.get('email')
    student = StudentInfo.objects.get(email=email)
    data = EnrolledCourses.objects.filter(email=email).all()
    for x in data:
        cd = CourseInfo.objects.filter(course_id=x.course_id).all()
        return render(request,'student/view_all_enrolled_classes.html',{'student':student,'data':cd})