from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from .models import Student,Parent,Faculty,HOD,Officestaff,AcceptedStudent,Acceptedfaculty,Grivence,AcceptedHOD,Bus,Notice

def index(request):
    al=Notice.objects.all()
    return render(request,'index.html',{'al':al})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



def principal_addteachers(request):
    return render(request,'principal_addteachers.html')

def principal_addhod(request):
    return render(request,'principal_addhod.html')

def principal_addofficestaff(request):
    return render(request,'principal_addofficestaff.html')



def principal_approveofficestaff(request):
    return render(request,'principal_approveofficestaff.html')

def principal_approvefaculty(request):
    return render(request,'principal_approvefaculty.html')

def academic_calender(request):
    return render(request,'academic_calender.html')




#student login & signup

global st
def studentlogin(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['pass']
        print(name)
        userinfo=AcceptedStudent.objects.all()
        for i in userinfo:
            if i.password2==password and i.name==name:
                global st
                def st():
                    return i.regno
                return render(request,'studentdashboard.html')
            else:
                pass
    return render(request,'studentlogin.html')
def studentsignup(request):
    if request.method=="POST":
        # rollno=request.POST['rollno']
        department=request.POST['department']
        regno=request.POST['regno']
        name=request.POST['name1']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(name)
        userinfo=Student(name=name,userid=email,password1=pass1,password2=pass2,department=department,regno=regno)
        userinfo.save()
        return render(request,'studentlogin.html')
    return render(request,'studentsignup.html')
def logout(request):
    return render(request,"index.html")
def studentdashboard(request):
    return render(request,'studentdashboard.html')


# Parent login & signup


def parentlogin(request):
    if request.method=="POST":
        name=request.POST['pname']
        password=request.POST['ppass']
        print(name)
        userinfo=Parent.objects.all()
        for i in userinfo:
            if i.ppassword==password and i.pname==name:
                return render(request,'studentdashboard.html')
            else:
                pass
    return render(request,'parentlogin.html')
def parentsignup(request):
    if request.method=="POST":
        pname=request.POST['pname']
        pemail=request.POST['pemail']
        ppass1=request.POST['ppass']
        pcpass2=request.POST['pcpass']
        print(pname)
        userinfo=Parent(pname=pname,pemail=pemail,ppassword=ppass1,parent_cpassword=pcpass2)
        userinfo.save()
        return render(request,'parentlogin.html')
    return render(request,'parentsignup.html')

# Faculty login & signup
global val

def facultylogin(request):
    if request.method=="POST":
        fname=request.POST['fname']
        fpassword=request.POST['fpassword']
        global val
        def val():
            return fname
        # print(name)
        userinfo=Acceptedfaculty.objects.all()
        for i in userinfo:
            if i.ffpassword==fpassword and i.ffname==fname:
                fyname=i.ffname
                finfo=Student.objects.all()
                return render(request,'facultydashboard.html',{'finfo':finfo,'fyname':fyname})
            else:
                pass
    return render(request,'facultylogin.html')
def facultysignup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        femail=request.POST['femail']
        fpassword=request.POST['fpassword']
        fnumber=request.POST['fnumber']
        faculty_cpassword=request.POST['faculty_cpassword']
        fdepartment=request.POST['fdepartment']
        userinfo=Faculty(fname=fname,femail=femail,fpassword=fpassword,fnumber=fnumber,faculty_cpassword=faculty_cpassword,fdepartment=fdepartment)
        userinfo.save()
        global val
        def val():
            return fname
        return render(request,'facultylogin.html')
    return render(request,'facultysignup.html')
def logout(request):
    return render(request,"index.html")
def facultydashboard(request):
    return render(request,'facultydashboard.html')


# HOD login & signup

global toget

def hodlogin(request):
    if request.method=="POST":
        name=request.POST['hname']
        password=request.POST['hpass']
        print(name)
        userinfo=AcceptedHOD.objects.all()
        for i in userinfo:
            if i.hhpassword==password and i.hhname==name:
                fyname=i.hhname
                global toget
                getdep=i.hhdepartment
                def toget():
                    return getdep
                de=i.hhdepartment
                finfo=Student.objects.filter(department=de)
                print(de)
                teachers=Faculty.objects.filter(fdepartment=de)
                return render(request,'hoddashboard.html',{'finfo':finfo,'fyname':fyname,'teachers':teachers})
            else:
                pass
    return render(request,'hodlogin.html')

def accept(request):
    if request.method=="POST":
        reg=request.POST['data']
        hodep=toget()
        userinfo=AcceptedHOD.objects.all()
        for i in userinfo:
            if i.hhdepartment==hodep:
                fyname=i.hhname
                break
        de=i.hhdepartment
        new=Student.objects.all()
        for j in new:
            if j.regno==reg:       
                userinfo=AcceptedStudent(name=j.name,userid=j.userid,password1=j.password1,password2=j.password2,department=j.department,regno=j.regno,fathername=1,mothername=1,guardianname=1,guardianphn=1,guardianemail=1,yearofjoining=1,gender=1,admissionno=1,dob=1,admissiontype=1,semester=1,present=1,absent=1,percentage=1,bus=0,busfee=0,avl=0)
                userinfo.save()
                finfo=Student.objects.get(regno=reg)
                finfo.delete()

                break
        finfo=Student.objects.filter(department=de)
        teachers=Faculty.objects.filter(fdepartment=de)
        return render(request,'hoddashboard.html',{'finfo':finfo,'fyname':fyname,'teachers':teachers})

def reject(request):
        if request.method=="POST":
            reg=request.POST['data']
            hodep=toget()
            userinfo=AcceptedHOD.objects.all()
            for i in userinfo:
                if i.hhdepartment==hodep:
                    fyname=i.hhname
                    break
            de=i.hhdepartment
            new=Student.objects.all()
            for j in new:
                if j.regno==reg:       
                    finfo=Student.objects.get(regno=reg)
                    finfo.delete()
                    break
            finfo=Student.objects.filter(department=de)
            teachers=Faculty.objects.filter(fdepartment=de)
            return render(request,'hoddashboard.html',{'finfo':finfo,'fyname':fyname,'teachers':teachers})  
def ffaccept(request):
    if request.method=="POST":
        nam=request.POST['data']
        hodep=toget()
        userinfo=AcceptedHOD.objects.all()
        for i in userinfo:
            if i.hhdepartment==hodep:
                fyname=i.hhname
                break
        de=i.hhdepartment
        new=Faculty.objects.all()
        for j in new:
            if j.fname==nam:       
                userinfo=Acceptedfaculty(ffname=j.fname,ffemail=j.femail,ffpassword=j.fpassword,ffdepartment=j.fdepartment,ffnumber=j.fnumber,ffaculty_cpassword=j.faculty_cpassword)
                userinfo.save()
                finfo=Faculty.objects.get(fname=nam)
                finfo.delete()
                break
        finfo=Student.objects.filter(department=de)
        teachers=Faculty.objects.filter(fdepartment=de)
        return render(request,'hoddashboard.html',{'finfo':finfo,'fyname':fyname,'teachers':teachers})
    return render(request,'hoddashboard.html')
def ffreject(request):
    if request.method=="POST":
            nam=request.POST['data']
            hodep=toget()
            userinfo=HOD.objects.all()
            for i in userinfo:
                if i.hdepartment==hodep:
                    fyname=i.hname
                    break
            de=i.hdepartment
            new=Faculty.objects.all()
            for j in new:
                if j.fname==nam:       
                    finfo=Faculty.objects.get(fname=nam)
                    finfo.delete()
                    break
            finfo=Student.objects.filter(department=de)
            teachers=Faculty.objects.filter(fdepartment=de)
            return render(request,'hoddashboard.html',{'finfo':finfo,'fyname':fyname,'teachers':teachers})  
    return render(request,'hoddashboard.html')
def hodsignup(request):
    if request.method=="POST":
        hname=request.POST['hname']
        hemail=request.POST['hemail']
        hnumber=request.POST['hnumber']
        hpass1=request.POST['hpass']
        hcpass2=request.POST['hcpass']
        hdepartment=request.POST['hdepartment']
        print(hname)
        userinfo=HOD(hname=hname,hemail=hemail,hpassword=hpass1,hod_cpassword=hcpass2,hnumber=hnumber,hdepartment=hdepartment)
        userinfo.save()
        return render(request,'hodlogin.html')
    return render(request,'hodsignup.html')

def logout(request):
    return render(request,"index.html")
def hoddashboard(request):
    return render(request,'hoddashboard.html')



# Officestaff login & signup



def officestafflogin(request):
    if request.method=="POST":
        name=request.POST['oname']
        password=request.POST['opass']
        print(name)
        userinfo=Officestaff.objects.all()
        for i in userinfo:
            if i.opassword==password and i.oname==name:
                return render(request,'officestaff1.html')
            else:
                pass
    return render(request,'officestafflogin.html')

def officestaffsignup(request):
    if request.method=="POST":
        oname=request.POST['oname']
        oemail=request.POST['oemail']
        opass1=request.POST['opass']
        ocpass2=request.POST['ocpass']
        if ocpass2!=opass1:
            return HttpResponse('<script>alert("Enter correctly ."); window.location.href = "officestaffsignup";</script>')
        print(oname)
        userinfo=Officestaff(oname=oname,oemail=oemail,opassword=opass1,officestaff_cpassword=ocpass2)
        userinfo.save()
        return HttpResponse('<script>alert("signup successfully."); window.location.href = "officestafflogin";</script>')

    return render(request,'officestafflogin.html')
def officestaff1(request):
    return render(request,'officestaff1.html')
def studentlist(request):
    year=request.POST['year']
    department=request.POST['department']
    stu = AcceptedStudent.objects.filter(yearofjoining=year,department=department)
    d = {'item' : stu}
    return render(request,'studentlist.html',d)

def officedashboard(request):
    return render(request,'officedashboard.html')
    


def logout(request):
    return render(request,"index.html")
def principallogin(request):
    if request.method=="POST":
        pprname=request.POST['prname']
        prpass=request.POST['prpass']
        name="cectl"
        ppass="123"
        if pprname==name and prpass==ppass:
            return HttpResponse('<script>alert("Login successfully."); window.location.href = "principaldashboard";</script>')

        else:
            return HttpResponse('<script>alert("Login error."); window.location.href = "principallogin";</script>')

        
    return render(request,'principallogin.html')
def officedashboard(request):
    return render(request,"officedashboard.html")
def principaldashboard(request):
    inf=Grivence.objects.all()
    tcount=Acceptedfaculty.objects.count()
    scount=AcceptedStudent.objects.count()
    return render(request,"principaldashboard.html",{'inf':inf,'tcount':tcount,'scount':scount})
def teacherprofile(request):
    fname=val()
    fac = Acceptedfaculty.objects.all()
    for i in fac:
        if fname == i.ffname:
            break
    return render(request,'teacherprofile.html',{'i':i})
def studentprofile(request):
    sregno=st()
    stc=AcceptedStudent.objects.all()
    for i in stc:
        if sregno==i.regno:
            break
    return render(request,"studentprofile.html",{'i':i})
def facultyassingment(request):
    return render(request,"facultyassingment.html")
def grivence(request):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name)
        try:
            x=Grivence.objects.get(gemail=email)
        except:    
            info=Grivence(gname=name,gemail=email,gsubject=subject,gmessage=message)
            info.save()
        
            print("success")
            return render(request,"contact.html")
        return render(request,"contact.html")
def principal_grievances(request):
        inf=Grivence.objects.all()
        return render(request,"principal_grievances.html",{'inf':inf})
def busfeeupdate(request):
    if request.method=="POST":
        tos=Bus.objects.all()
        route=request.POST['route']
        fee=request.POST['fee']
        for i in tos:
            if i.to==route:
                break
        i.busfees=fee
        i.save()
        lists=AcceptedStudent.objects.filter(avl=1)
        nlists=AcceptedStudent.objects.filter(avl=0)
        return render(request,"busfeeupdate.html",{'tos':tos,'lists':lists,'nlists':nlists})
    lists=AcceptedStudent.objects.filter(avl=1)
    nlists=AcceptedStudent.objects.filter(avl=0)
    tos=Bus.objects.all()
    return render(request,"busfeeupdate.html",{'tos':tos,'lists':lists,'nlists':nlists})
def examfeeupdate(request):
    return render(request,"examfeeupdate.html")
def principal_approvehod(request):
    info=HOD.objects.all()
    return render(request,'principal_approvehod.html',{'info':info})
def haccept(request):
    if request.method=="POST":
        hnam=request.POST['data']
        new=HOD.objects.all()
        for j in new:
            if j.hname==hnam:       
                userinfo=AcceptedHOD(hhname=j.hname,hhemail=j.hemail,hhnumber=j.hnumber,hhpassword=j.hpassword,hhdepartment=j.hdepartment,hhod_cpassword=j.hod_cpassword)
                userinfo.save()
                finfo=HOD.objects.get(hname=hnam)
                finfo.delete()
                break
        info=HOD.objects.all()
        return render(request,'principal_approvehod.html',{'info':info})
    return render(request,'principal_approvehod.html')
def hreject(request):
    if request.method=="POST":
            hnam=request.POST['data']
            new=HOD.objects.all()
            for j in new:
                if j.hname==hnam:       
                    finfo=HOD.objects.get(hname=hnam)
                    finfo.delete()
                    break
            info=HOD.objects.all()
            return render(request,'principal_approvehod.html',{'info':info})  
    return render(request,'principal_approvehod.html')
def busroute(request):
    tos=Bus.objects.all()
    name=st()
    check=AcceptedStudent.objects.all()
    for i in check:
        i.regno=name
        break
    if i.busfee==1:
        msg="busfee is payed"
    else:
        msg="busfee is not payed"
    stop=i.bus

    if request.method=="POST":
        tos=Bus.objects.all()
        route=request.POST['route']
        name=st()
        check=AcceptedStudent.objects.all()
        for i in check:
            i.regno=name
            print(name)
            print(i.regno)
            print(route)
            break
        print(i.bus)
        i.bus=route
        i.avl=1
        i.save()
        stop=i.bus
        for i in tos:
            i.to=route
            break
        fe=i.busfees

        return render(request,'busroute.html',{'msg':msg,'tos':tos,'stop':stop,'fe':fe})

    return render(request,'busroute.html',{'msg':msg,'tos':tos,'stop':stop})
global to
def replays(request):
    if request.method=="POST":

        tmail=request.POST['tmail']
        global to
        def to():
            return tmail
        return render(request,"replay.html")
def replayed(request):
    if request.method=="POST":
        subject=request.POST['subject']
        message=request.POST['message']
        print(subject)
        print(message)
        try:
            import smtplib
            from email.message import EmailMessage

            # Create a message object
            msg = EmailMessage()
            tos=to()
            # Set the sender, recipient, subject, and body of the message
            msg['From'] = 'eduhubcectl@gmail.com'
            msg['To'] =to()
            msg['Subject'] =subject
            msg.set_content(message)

            # Connect to the SMTP server
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()

            # Login to your email account
            username = 'eduhubcectl@gmail.com'
            password = 'tpucdcdskwfmmxtt'
            smtp_server.login(username, password)

            # Send the message
            smtp_server.send_message(msg)

            # Disconnect from the SMTP server
            smtp_server.quit()

            print('Email sent successfully!')
            finfo=Grivence.objects.get(gemail=tos)
            finfo.delete()
            inf=Grivence.objects.all()
        except:
            print("errorr")
            pass
        return render(request,"principal_grievances.html",{'inf':inf})
def toteacher(request):
    tot=Acceptedfaculty.objects.all()
    return render(request,"toteacher.html",{'tot':tot})
def tostudent(request):
    tos=AcceptedStudent.objects.all()
    return render(request,"tostudent.html",{'tos':tos})
def principal_notice(request):
    if request.method=="POST":
        notes=request.POST['notes']
        noted=Notice(note=notes)
        noted.save()
        tcount=Acceptedfaculty.objects.count()
        scount=AcceptedStudent.objects.count()
        return render(request,"principaldashboard.html",{'tcount':tcount,'scount':scount})
    return render(request,'principal_notice.html')
