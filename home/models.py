from django.db import models

# Create your models here.
class Student(models.Model):
    # rollno=models.IntegerField()
    regno=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    name=models.CharField(max_length=10)
    userid=models.CharField(max_length=100)
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name
class AcceptedStudent(models.Model):
    # rollno=models.IntegerField()
    regno=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    name=models.CharField(max_length=10)
    userid=models.CharField(max_length=100)
    present=models.IntegerField()
    absent=models.IntegerField()
    percentage=models.IntegerField()
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    fathername=models.CharField(max_length=10)
    mothername=models.CharField(max_length=10)
    guardianname=models.CharField(max_length=10)
    guardianphn=models.CharField(max_length=10)
    guardianemail=models.CharField(max_length=10)
    yearofjoining=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    admissionno=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
    admissiontype=models.CharField(max_length=10)
    semester=models.CharField(max_length=10)

class Parent(models.Model):
    pname=models.CharField(max_length=10)
    pemail=models.CharField(max_length=10)
    pphonenumber=models.IntegerField(max_length=10)
    name=models.CharField(max_length=10)
    ppassword=models.CharField(max_length=10)
    parent_cpassword=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    fname=models.CharField(max_length=100)
    femail=models.CharField(max_length=100)
    fdepartment=models.CharField(max_length=100)
    fnumber=models.IntegerField(max_length=100)
    fpassword=models.CharField(max_length=100)
    faculty_cpassword=models.CharField(max_length=100)

    def __str__(self):
        return self.fname
class Acceptedfaculty(models.Model):
    ffname=models.CharField(max_length=100)
    ffemail=models.CharField(max_length=100)
    ffdepartment=models.CharField(max_length=100)
    ffnumber=models.IntegerField(max_length=100)
    ffpassword=models.CharField(max_length=100)
    ffaculty_cpassword=models.CharField(max_length=100)

class HOD(models.Model):
    hname=models.CharField(max_length=100)
    hemail=models.CharField(max_length=100)
    hnumber=models.CharField(max_length=100)
    hdepartment=models.CharField(max_length=100)
    hpassword=models.CharField(max_length=100)
    hod_cpassword=models.CharField(max_length=100)
class AcceptedHOD(models.Model):
    hhname=models.CharField(max_length=100)
    hhemail=models.CharField(max_length=100)
    hhnumber=models.CharField(max_length=100)
    hhdepartment=models.CharField(max_length=100)
    hhpassword=models.CharField(max_length=100)
    hhod_cpassword=models.CharField(max_length=100)

    def __str__(self):
        return self.hname

class Officestaff(models.Model):
    oname=models.CharField(max_length=10)
    oemail=models.CharField(max_length=10)
    onumber=models.IntegerField(max_length=10)
    opassword=models.CharField(max_length=10)
    officestaff_cpassword=models.CharField(max_length=10)

    def __str__(self):
        return self.oname
class Grivence(models.Model):
    gname=models.CharField(max_length=10)
    gemail=models.CharField(max_length=100)
    gsubject=models.CharField(max_length=100)
    gmessage=models.CharField(max_length=100)
