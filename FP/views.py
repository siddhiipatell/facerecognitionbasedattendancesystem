from FBSA.models import Contact, F_Registration, Department, Gender, Semester, F_login, S_registration, S_Login, S_code, \
    F_code, Subject

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
from tkinter import *
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
from datetime import date
import time
import json
import glob



########## Home Data ###############################################################################################


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        c = Contact(name=name, email=email, subject=subject, message=message)
        c.save()
    return render(request, 'index.html')


########## Faculty Data ###############################################################################################

############## Faculty Registration ###################################

def f_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department1 = request.POST['department']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        n_pass = request.POST['n_pass']
        c_pass = request.POST['c_pass']
        f = F_Registration(first_name=first_name, last_name=last_name, department=department1,
                           gender=gender, email=email, phone=phone, n_pass=n_pass, c_pass=c_pass)
        f.save()
        log = F_login(email=email, c_pass=c_pass)
        log.save()
        messages.success(request, "Successfully registered")
        return redirect('F_login')
    dept = Department.objects.all()
    gen = Gender.objects.all()
    sem = Semester.objects.all()
    return render(request, 'f_registration.html', {'dept': dept, 'gen': gen, 'sem': sem})


###################### Faculty Login ####################


def f_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        c_pass = request.POST['c_pass']
        user = F_login.objects.filter(email=email)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('F_login')
        else:
            for e in user:
                if email == e.email and c_pass == e.c_pass:
                    request.session['email'] = email
                    return redirect('Faculty')
                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('F_login')
    return render(request, 'F_login.html')



######################### Faculty Home page ######################################

def faculty(request):
    sub_name=''
    if request.method == 'POST':
        code = request.POST['code']
        faculty.t1 = time.time()
        sub_name = request.POST['sub_name']
        request.session['code'] = code
        f_c = F_code(code=code, sub_name=sub_name)
        f_c.save()
        a_c = S_code(code=code, sub_name=sub_name)
        a_c.save()
        messages.success(request,"Your Code is generated")
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = F_Registration.objects.filter(email=email)
        subname = Subject.objects.all()
        dept = Department.objects.all()
        gen = Gender.objects.all()
        return render(request, 'Faculty.html', {'res': s,'subname': subname,'dept':dept,'gen':gen})
    else:
        redirect('F_login')




########## Student Data ###############################################################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)


def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()


def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids


############## student Registration ###################################

def s_registration(request):
    if request.method == 'POST':
        name = request.POST['s_fname']
        department1 = request.POST['department']
        sem1 = request.POST['sem']
        Id = request.POST['e_no']
        gender1 = request.POST['gender']
        b_date = request.POST['b_date']
        email = request.POST['email']
        phone = request.POST['phone']
        n_pass = request.POST['n_pass']
        c_pass = request.POST['c_pass']
        s = S_registration(s_fname=name, department=department1, e_no=Id,
                           sem=sem1, b_date=b_date, gender=gender1, email=email, phone=phone, n_pass=n_pass,
                           c_pass=c_pass)
        s.save()
        log = S_Login(email=email, c_pass=c_pass)
        log.save()
        messages.success(request, "Successfully registered")

        check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '']
        assure_path_exists("StudentDetails/")
        assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()

        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(40) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 40:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, '', Id, '', name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                message.configure(text=res)
        return redirect('capture')
    dept = Department.objects.all()
    gen = Gender.objects.all()
    sem = Semester.objects.all()
    return render(request, 'S_registration.html', {'dept': dept, 'gen': gen, 'sem': sem})


###################### student Login ####################

def s_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        c_pass = request.POST['c_pass']
        user = S_Login.objects.filter(email=email)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('S_Login')
        else:
            for e in user:
                if email == e.email and c_pass == e.c_pass:
                    request.session['email'] = email
                    return redirect('student')
                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('S_Login')
    return render(request, 'S_Login.html')



######################### student Homepage ######################################


def take_attendance(code, sub_name):
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")

    recognizer = cv2.face_LBPHFaceRecognizer.create()
    exists3 = os.path.isfile("TrainingImageLabel/Trainner.yml")

    if exists3:
        recognizer.read("TrainingImageLabel/Trainner.yml")
    else:
        messages.error('Data Missing', 'Please click on Save Profile to reset data!')
        return

    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time', '', 'Subject']

    exists1 = os.path.isfile("StudentDetails/StudentDetails.csv")

    if exists1:
        df = pd.read_csv("StudentDetails/StudentDetails.csv")
    else:
        messages.error('Details Missing', 'Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        return

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])

            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[2:-2]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [ID, '', bb, '', str(date), '', str(timeStamp), '', sub_name]
            else:
                Id = 'Unknown'
                bb = str(Id)

            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        
        cv2.imshow('Taking Attendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
    attendance_file = f"Attendance/Attendance_{sub_name}.csv"
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time', '', 'Subject']

    if os.path.isfile(attendance_file):
        with open(attendance_file, 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
    else:
        with open(attendance_file, 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)

    cam.release()
    cv2.destroyAllWindows()
# def student(request):
#     if request.session.has_key('email'):
#         email = request.session.get('email')
#         s = S_registration.objects.filter(email=email)
#         if request.method == 'POST':
#             code = request.POST['code']
#             t2 = time.time()
#             #sub_name= faculty()
#             user1 = S_code.objects.filter(code=code)
#             for fe in user1:
#                 if code == fe.code:
#                     sub_name=fe.sub_name
#                     if (t2 - faculty.t1) < 120:

def student(request):
    if 'email' in request.session:
        email = request.session['email']
        s = S_registration.objects.filter(email=email)

        if request.method == 'POST':
            code = request.POST.get('code')
            t2 = time.time()

            user1 = S_code.objects.filter(code=code)
            for fe in user1:
                if code == fe.code:
                    sub_name = fe.sub_name
                    if (t2 - faculty.t1) < 120:
                        take_attendance(code, sub_name)

                        # c = S_code.objects.filter(code=code)
                        # check_haarcascadefile()
                        # assure_path_exists("Attendance/")
                        # assure_path_exists("StudentDetails/")
                        # i = 0
                        # recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                        # exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
                        # if exists3:
                        #     recognizer.read("TrainingImageLabel\Trainner.yml")
                        # else:
                        #     mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
                        #     return
                        # harcascadePath = "haarcascade_frontalface_default.xml"
                        # faceCascade = cv2.CascadeClassifier(harcascadePath);

                        # cam = cv2.VideoCapture(0)
                        # font = cv2.FONT_HERSHEY_SIMPLEX
                        # col_names = ['Id', '', 'Name', '', 'Date', '', 'Time','','Subject']
                        # exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
                        # if exists1:
                        #     df = pd.read_csv("StudentDetails\StudentDetails.csv")
                        # else:
                        #     mess._show(title='Details Missing', message='Students details are missing, please check!')
                        #     cam.release()
                        #     cv2.destroyAllWindows()
                        #     window.destroy()
                        # while True:
                        #     ret, im = cam.read()
                        #     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        #     faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                        #     for (x, y, w, h) in faces:
                        #         cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                        #         serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        #         if (conf < 50):
                        #             ts = time.time()
                        #             date = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
                        #             timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        #             aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                        #             ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                        #             ID = str(ID)
                        #             ID = ID[2:-2]
                        #             bb = str(aa)
                        #             bb = bb[2:-2]
                        #             attendance = [ID, '', bb, '', str(date), '', str(timeStamp),'',sub_name]
                        #         else:
                        #             Id = 'Unknown'
                        #             bb = str(Id)
                        #         cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                        #     cv2.imshow('Taking Attendance', im)
                        #     if (cv2.waitKey(1) == ord('q')):
                        #         break
                        # ts = time.time()
                        # date = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
                        # exists = os.path.isfile("Attendance\Attendance_"+ sub_name + ".csv")
                        # if exists:
                        #     with open("Attendance\Attendance_"  + sub_name + ".csv", 'a+') as csvFile1:
                        #         writer = csv.writer(csvFile1)
                        #         writer.writerow(attendance)
                        #     csvFile1.close()
                        # else:
                        #     with open("Attendance\Attendance_"  + sub_name + ".csv", 'a+') as csvFile1:
                        #         writer = csv.writer(csvFile1)
                        #         writer.writerow(col_names)
                        #         writer.writerow(attendance)
                        #     csvFile1.close()
                        # with open("Attendance\Attendance_" +  sub_name + ".csv", 'r') as csvFile1:
                        #     reader1 = csv.reader(csvFile1)

                        # csvFile1.close()
                        # cam.release()
                        # cv2.destroyAllWindows()
                        messages.success(request, 'Attendance Marked Successfully')
                        return render(request, 'student.html', {'res': s})
                    else:
                        messages.error(request, "Your code has expired!")
                        return redirect("student")
        dept = Department.objects.all()
        gen = Gender.objects.all()
        sem = Semester.objects.all()
        return render(request, 'student.html', {'res': s,'dept': dept, 'gen': gen, 'sem': sem})
    else:
        return redirect('S_Login')


def capture(request):
    if request.method == 'POST':
        check_haarcascadefile()
        assure_path_exists("TrainingImageLabel/")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Profile Saved Successfully"
        return redirect('S_Login')
    return render(request, 'capture.html')


def datatable(request, file):
    csv_fp = open('Attendance/{Attendance}.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'datatable.html', {'data': out, 'headers': headers})


def f_logout(request):
    if request.method == 'POST':
        return redirect('F_login')


def s_logout(request):
    if request.method == 'POST':
        return redirect('S_Login')

def viewAttendance(request):
    if request.method == 'POST':
        code = request.POST['code']
        sub_name = request.POST['sub_name']
        request.session['code'] = code
        f_c = F_code(code=code, sub_name=sub_name)
        f_c.save()
        a_c = S_code(code=code, sub_name=sub_name)
        a_c.save()


    if request.session.has_key('email'):
        email = request.session.get('email')
        s = F_Registration.objects.filter(email=email)
        subname = Subject.objects.all()
        dept = Department.objects.all()
        gen = Gender.objects.all()
        return render(request, 'viewAttendance.html', {'res': s,'subname': subname,'dept':dept,'gen':gen})
    else:
        redirect('F_login')

def viewA(request):
    if request.method == 'POST':
        sub_name = request.POST['sub_name']
        filename = 'Attendance\Attendance_' + sub_name + '.csv'
        d2 = date.today()
        d1 = d2.strftime("%m-%d-%Y")
        df = pd.read_csv(filename)
        todaydf = df[(df['Date'] == d1)].index
        attendance = pd.DataFrame()
        for i in todaydf:
            # display=display(df.iloc[i])
            attendance = attendance.append(df.iloc[i])
        att1= attendance[['Id','Name','Date','Time','Subject']]
        attendance1 = att1.to_html
        subname = Subject.objects.all()
        return render(request,'viewAttendance.html',{'d':attendance1,'subname':subname})


def monthAttendance(request):
    if request.method == 'POST':
        code = request.POST['code']
        sub_name = request.POST['sub_name']
        request.session['code'] = code
        f_c = F_code(code=code, sub_name=sub_name)
        f_c.save()
        a_c = S_code(code=code, sub_name=sub_name)
        a_c.save()


    if request.session.has_key('email'):
        email = request.session.get('email')
        s = F_Registration.objects.filter(email=email)
        subname = Subject.objects.all()
        dept = Department.objects.all()
        gen = Gender.objects.all()
        return render(request, 'monthAttendance.html', {'res': s,'subname': subname,'dept':dept,'gen':gen})
    else:
        redirect('F_login')


def month(request):
    if request.method == 'POST':
        sub_name = request.POST['sub_name']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        filename = 'Attendance\Attendance_' + sub_name + '.csv'
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])
        df['day'] = df['Date'].dt.day
        df['Month'] = df['Date'].dt.month
        index1 = df[((df['Date'] >= fdate) & (df['Date'] <= tdate))].index

        attendance = pd.DataFrame()
        for i in index1:
            # display=display(df.iloc[i])
            attendance = attendance.append(df.iloc[i])
        att1 = attendance[['Id', 'Name', 'Date', 'Time', 'Subject']]
        var1 = att1['Id'].value_counts()
        var2 = 15
        result = round(((var1 / var2) * 100), 2)
        z1 = var1.to_dict()
        z2 = result.to_dict()
        df2 = pd.DataFrame()
        Id = df['Id'].unique()
        Name = df['Name'].unique()
        df2['Id'] = Id
        df2['Name'] = Name
        df2['Lectures Attended'] = df2['Id'].map(z1)
        df2['Percentage'] = df2['Id'].map(z2)
        data = df2.to_html
        subname = Subject.objects.all()
        return render(request, 'monthAttendance.html', {'subname': subname, 'data': data})


def editprofile(request):
    if request.method == 'POST':
        # sem1 = request.POST['sem']
        # b_date = request.POST['b_date']
        phone = request.POST['phone']
        if request.session.has_key('email'):
            email = request.session.get('email')
            s1 = S_registration.objects.filter(email=email)
        for record in s1:
            # record.sem = sem1
            # record.b_date = b_date
            record.phone = phone
            record.save(update_fields=['phone'])
            messages.success(request, "Profile Updated Successflly")
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = S_registration.objects.filter(email=email)
        dept = Department.objects.all()
        gen = Gender.objects.all()
        sem = Semester.objects.all()
        return render(request, 'editprofile.html', {'res': s, 'dept': dept, 'gen': gen, 'sem': sem})
    else:
        redirect('S_Login')

def editprofile1(request):
    if request.method == 'POST':
        # name = request.POST['first_name']
        # name1 = request.POST['last_name']
        phone = request.POST['phone']
        if request.session.has_key('email'):
            email = request.session.get('email')
            s1 = F_Registration.objects.filter(email=email)
        for record in s1:
            # record.first_name = name
            # record.last_name = name1
            record.phone = phone
            record.save(update_fields=['phone'])
            messages.success(request, "Profile Updated Successfully")
    if request.session.has_key('email'):
        email = request.session.get('email')
        f = F_Registration.objects.filter(email=email)
        dept = Department.objects.all()
        gen = Gender.objects.all()
        return render(request, 'editprofile1.html', {'res': f, 'dept': dept, 'gen': gen})
    else:
        redirect('F_login')