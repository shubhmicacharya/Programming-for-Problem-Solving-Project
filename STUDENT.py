import csv

def create_student():
    ans='y'
    while(ans=='y'):
        stu_id=input("Enter Student ID:")
        name=input("Enter Name of Student:")
        roll=input("Enter Class Roll Number:")
        batch_id=input("Enter Batch ID:")
        stu=open("Student.csv","a+")
        sw=csv.writer(stu)
        sw.writerow([stu_id,name,roll,batch_id])
        stu.close()
        ans=input("Do you want to enter more records?....(y/n):")
    print("Showing your File........")
    stu=open("Student.csv","r",newline="\r\n")
    stu.seek(0)
    sw=csv.reader(stu)
    for row in sw:
        print(row)
    stu.close()

def update_student():
    stu=open("Student.csv","r",newline="\r\n")
    sw=csv.reader(stu)
    l=[]
    check=input("Enter Student ID:")
    print("Enter 1 for updating Name")
    print("Enter 2 for updating Class Roll No.")
    print("Enter 3 for updating Batch_ID")
    ch=input("Enter your choice:")
   
    for row in sw:
        if row[0]==check:
             new=input("Enter new data:")
             row[int(ch)]=new
        l.append(row)
    stu.close()
    stu=open("Student.csv","w")
    sw=csv.writer(stu)
    sw.writerows(l)
    stu.close()
    print("Showing your Updated File........")
    stu=open("Student.csv","r",newline="\r\n")
    stu.seek(0)
    sw=csv.reader(stu)
    for row in sw:
        print(row)
    stu.close()

def remove_student():
    stu=open("Student.csv","r",newline="\r\n")
    sw=csv.reader(stu)
    l=[]
    check=input("Enter Student ID of student to be removed:")
    found=False
    for row in sw:
        if row[0]==check:
            found=True
        else:
            l=l.append(row)
    stu.close()
    stu=open("Student.csv","a+")
    sw=csv.writer(stu)
    sw.writerows(l)
    stu.close()
    print("Showing your File after REMOVAL........")
    stu=open("Student.csv","r",newline="\r\n")
    stu.seek(0)
    sw=csv.reader(stu)
    for row in sw:
        print(row)
    stu.close()

def result():
    c=input("Enter name of Student:")
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    f=False
    d={}
    for row in crsr:
        if row[2]=="Marks Obtained":
            f=True
        else:
            for i in row[2]:
                d=i
                if d["Student Name"]==c:
                    print(d)
                    if int(d["Marks"])>=90:
                        print("GRADE-A..............PASS")
                    elif int(d["Marks"])>=80:
                        print("GRADE-B..............PASS")
                    elif int(d["Marks"])>=70:
                        print("GRADE-C..............PASS")
                    elif int(d["Marks"])>=60:
                        print("GRADE-D..............PASS")
                    elif int(d["Marks"])>=50:
                        print("GRADE-E..............PASS")
                    elif int(d["Marks"])<40:
                        print("GRADE-F..............FAIL")



