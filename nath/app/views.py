from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import classroom,student,opt,student_marks
from django.contrib.auth.models import User
from django.contrib.auth.models import User,auth
from django.contrib import messages


#for parents 
def class_room(request):
	if request.user.username == 'some':
		return redirect('class_for_school')
	classrooms = classroom.objects.all()
	return render(request
		,'class.html',{'cr':classrooms})

#show students for parents
def show_students(request,pk):
	stus = student.objects.filter(stu_class=pk)

	c = classroom.objects.filter(c=pk).first()
	return render(request,'show_students.html',{'s':stus,'c':c})


#show clas for school 
def class_for_school(request):
	classrooms = classroom.objects.all()
	return render(request,'classforschool.html',{'cr':classrooms})
def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		userdata = User.objects.create_user(username=username,password=password)
		userdata.save()
		print('saved')
		return redirect('login')
	return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		userdata = auth.authenticate(username=username,password=password)
		if userdata is not None:
			auth.login(request,userdata)
			return redirect('/')
		else:
			return redirect('login')
	return render(request,'login.html')

def detail(request,pk):

	detailgo = classroom.objects.get(id=pk)
	class_num = classroom.objects.filter(id=pk).first()
	students_list = student.objects.filter(stu_class=pk)
	print(students_list)
	return render(request,'class_detail.html',{'i':class_num,'students':students_list})

#adding student into database
def addstudent(request):
	if request.method == 'POST':
		s_id=request.POST.get('s_id')
		student_name = request.POST.get('stu_name')
		student_class = request.POST.get('stu_class')
		student_phone = request.POST.get('phonenumber')
		student_roll = request.POST.get('roll_num')
		password = request.POST.get('password')
		print(s_id)
		if (s_id!=''):
			
			s = student.objects.get(id=s_id)
			s_id=request.POST.get('s_id')
			
			student_db_data_save = student(
				id=s_id,
				stu_name=student_name,
				stu_class=student_class,
				phone_number=student_phone,
				roll_num=student_roll)
			
			student_db_data_save.save()

			students = student.objects.filter(stu_class=student_class).order_by('stu_name')
			return JsonResponse({'students':list(students.values()),'successed':'Student Name added successfully'})					

		else:

			student_db_data = student(
				
				stu_name=student_name,
				stu_class=student_class,
				phone_number=student_phone,
				roll_num=student_roll)
			
			student_db_data.save()
			students = student.objects.filter(stu_class=student_class).order_by('stu_name')
			return JsonResponse({'students':list(students.values()),'successed':'Student Name added successfully'})

		return JsonResponse({'status':'saved'})

#delete student
def deletestudent(request):
	if request.method == 'POST':
		id = request.POST.get('sid')
		stu_c = request.POST.get('stu_c')
		student_id = student.objects.get(pk=id)
		stu.delete()
		student_id.delete()
		

		students = student.objects.filter(stu_class=stu_c).order_by('stu_name')
		return JsonResponse({'status':1,'students':list(students.values())})
	else:
		return JsonResponse({'status':0})

#editstudent
def editstudent(request):
	if request.method == 'POST':
		id = request.POST.get('sid')
		sid = student.objects.get(pk=id)
		students = {'id':sid.id,'stu_name':sid.stu_name,'stu_class':sid.stu_class,'roll_num':sid.roll_num,'phonenumber':sid.phone_number}
		
		
	return JsonResponse(students)


#getting data of student name to login for user or parent
def show_student_name_login(request):
	if request.method == 'POST':
		show_student = request.POST.get('stu_name')
	else:
		show_student = ''
	print(show_student)
	student_data = student.objects.filter(stu_name__contains=show_student)
	return JsonResponse({'students':list(student_data.values())})

def logout(request):
	auth.logout(request)
	return redirect('/')
	return HttpResponse('logout')

#student page 
def studentpage(request,pk):
	stu_id = student.objects.get(id=pk)
	print(stu_id.stu_name)
	marks_students = student_marks.objects.filter(stu_id=pk).order_by('test_num')
	return render(request,'studentpage.html',{'marks':marks_students,'s_name':stu_id})

#on click on add btn to fill student name
def fill_stu(request):
	if request.method == 'POST':
		id = request.POST.get('btnid')
		student_data = student.objects.get(pk=id)
		stu = {'id':student_data.id,'stu_name':student_data.stu_name}
		return JsonResponse(stu)

#on click students will appear
def show_students_data_mouse_click(request):
	if request.method == 'POST':
		stu_class = request.POST.get('stu_class')
		students = student.objects.filter(stu_class=stu_class).order_by('stu_name')
		return JsonResponse({'students':list(students.values())})
	return JsonResponse({'status':'working'})

#get student data to enter in marks form
def get_stu_data_to_marks(request):
	if request.method == 'POST':
		stu_id = request.POST.get('sid')
		stu = student.objects.get(pk=stu_id)
		stu_data = {
		'id':stu.id,
		'stu_name':stu.stu_name,
		'stu_class':stu.stu_class
		}
	return JsonResponse(stu_data)

#save marks of students
def save_student_marks(request):
	if request.method == 'POST':
		sid = request.POST.get('id')
		stu_id = request.POST.get('stu_id')
		stu_name=request.POST.get('stu_name')
		lwrt = request.POST.get('lwrt')
		telugu = request.POST.get('telugu')
		hindi = request.POST.get('hindi')
		english = request.POST.get('english')
		maths= request.POST.get('maths')
		physics = request.POST.get('physics')
		biology = request.POST.get('biology')
		social = request.POST.get('social')
		sanskrit = request.POST.get('sanskrit')
		total = request.POST.get('total')
		percent = request.POST.get('percent')
		p = format(percent,'.4')
		print(p)
		ta = request.POST.get('ta')
		ma = request.POST.get('ma')
		ha = request.POST.get('ha')
		ea = request.POST.get('ea')
		pa = request.POST.get('pa')
		ba = request.POST.get('ba')
		sa = request.POST.get('sa')
		sana = request.POST.get('sana')
	
		if (sid==''):
			data_save = student_marks(

					stu_id=stu_id,
					stu_name=stu_name,
					test_num=lwrt,
					telugu=telugu,
					hindi=hindi,
					english=english,
					maths=maths,
					physic=physics,
					biology=biology,
					social=social,
					sanskrit=sanskrit,
					total=total,
					percent=p,
					ta=ta,
					ma=ma,
					ha=ha,
					ea=ea,
					pa=pa,
					ba=ba,
					sa=sa,
					sana=sana
				)
			data_save.save()
			stu_get = student_marks.objects.filter(stu_id=stu_id).order_by('test_num')
			return JsonResponse({'stu_marks':list(stu_get.values())})
			
		else:
			p = format(percent,'.4')
			data_save = student_marks(
					id=sid,
					stu_id=stu_id,
					stu_name=stu_name,
					test_num=lwrt,
					telugu=telugu,
					hindi=hindi,
					english=english,
					maths=maths,
					physic=physics,
					biology=biology,
					social=social,
					sanskrit=sanskrit,
					total=total,
					percent=p,
					ta=ta,
					ma=ma,
					ha=ha,
					ea=ea,
					pa=pa,
					ba=ba,
					sa=sa,
					sana=sana
				)
			data_save.save()
			stu_get = student_marks.objects.filter(stu_id=stu_id).order_by('test_num')
			return JsonResponse({'stu_marks':list(stu_get.values())})
	return JsonResponse({'status':'saved'})

#show student marks for school
def show_student_marks_for_school(request):
	if request.method == 'POST':
		id = request.POST.get('id')
		student_get = student.objects.get(pk=id)
		student_marks_list = student_marks.objects.filter(stu_id=student_get.id).order_by('test_num')
		print(student_marks_list)
	return JsonResponse({'status':'showing','stu_marks':list(student_marks_list.values())})

#editing student marks
def editmarks(request):
	if request.method == 'POST':
		id = request.POST.get('mid')
		stu_get = student_marks.objects.get(pk=id)
		stu_edit_get = {
		'id':stu_get.id,
		'stu_id':stu_get.stu_id,
		'test_num':stu_get.test_num,
		'telugu':stu_get.telugu,
		'maths':stu_get.maths,
		'hindi':stu_get.hindi,
		'english':stu_get.english,
		'physics':stu_get.physic,
		'biology':stu_get.biology,
		'social':stu_get.social,
		'sanskrit':stu_get.sanskrit,
		'total':stu_get.total,
		'ta':stu_get.ta,
		'ma':stu_get.ma,
		'ha':stu_get.ha,
		'ea':stu_get.ea,
		'pa':stu_get.pa,
		'ba':stu_get.ba,
		'sa':stu_get.sa,
		'sana':stu_get.sana,
		'percent':stu_get.percent
				}
	return JsonResponse(stu_edit_get)


#delete marks
def deletemarks(request):
	if request.method == 'POST':
		id = request.POST.get('mid')
		stu_id = request.POST.get('stu_id')
		stu_marks = student_marks.objects.filter(stu_id=stu_id).order_by('test_num')
		print(stu_marks)
		marks_id = student_marks.objects.get(pk=id)
		marks_id.delete()
		
		return JsonResponse({'status':1,'stu_marks':list(stu_marks.values())})
	else:
		return JsonResponse({'status':0})

def some(request):
	responseData = sms.send_message(
    	{
        	"from": "Vonage APIs",
        	"to": "917893895732",
        	"text": "A text message sent using the Nexmo SMS API",
   	 	}
	)

	if responseData["messages"][0]["status"] == "0":

    		print("Message sent successfully.")
	else:
    		print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
	return HttpResponse('hi')



def search(request):
	if request.method == 'POST':
		searched_student = request.POST.get('search')
		stu_class = request.POST.get('stu_class')
	
		students = student.objects.filter(stu_name__contains=searched_student,stu_class=stu_class)
		return JsonResponse({'data':'data','students':list(students.values())})

