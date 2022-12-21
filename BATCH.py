import csv
import matplotlib.pyplot as plt
batch=open("Batch.csv","a")
batchw=csv.writer(batch)
batchw.writerow(["Batch ID","Batch Name","Department Name,","List of Courses","List of Students"])
batch.close()

def create_batch():
    ans="y"
    while ans=="y":
        batch_id=input("Enter Batch ID:")
        batch_name=input("Enter Batch Name:")
        dept_name=input("Enter Department Name:")
        c_l=[]
        a="Y"
        while a=="Y":
            course=input("Enter course:")
            c_l=c_l.append(course)
            a=input("Do you want to add more courses?..........(Y/N)")
        s_l=[]
        b="Y"
        while b=="Y":
            student=input("Enter Student ID:")
            s_l=s_l.append(student)
            b=input("Do you want to add more students?..........(Y/N)")
        batch=open("Batch.csv","a")
        batchw=csv.writer(batch)
        batchw.writerow([batch_id,batch_name,dept_name,c_l,s_l])
        batch.close()
        ans=input("Do you want to add more data?..........(y/n)")

def student_list():
    batch=open("Batch.csv","r",newline="\r\n")
    batch.seek(0)
    found=False
    batchr=csv.reader(batch)
    for row in batchr:
        if row[4]=="List of Students":
            found=True
        else:
            print(row[4])
    batch.close()

def course_list():
    batch=open("Batch.csv","r",newline="\r\n")
    batch.seek(0)
    found=False
    batchr=csv.reader(batch)
    for row in batchr:
        if row[3]=="List of Courses":
            found=True
        else:
            print(row[3])
    batch.close()

def performance():
    l=[]
    b=[]
    btname=input("Enter batch name:")
    batch=open("Batch.csv","r",newline="\r\n")
    batch.seek(0)
    batchr=csv.reader(batch)
    for row in batchr:
        if row[1]==btname:
            l=l.append(row[4])
    batch.close()
    stu=open("Student.csv","r",newline="\r\n")
    stu.seek(0)
    stur=csv.reader(stu)
    for row in l:
        for r in stur:
            if row==r[0]:
                b=b.append(r[1])
    stu.close()
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    d={}
    f=False
    for row in b:
        for r in crsr:
            if r[2]=="Marks Obtained":
                f=True
            else:
                d=r[2]
            if row==d["Student Name"]:
                print(d)

def pie_chart():
    batch=open("Batch.csv","r",newline="\r\n")
    batch.seek(0)
    batchr=csv.reader(batch)
    f=False
    l=[]
   
    for row in batchr:
        if row[0]=="Batch ID":
            f=True
        else:
            l.append(row[3])
           
    batch.close()
    fl=False
    
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    l2=[]
    l1=[]
    for r in crsr:
        
        
        if r[0]=="Course ID":
            fl=True
        else:
            for b in l:
                
                if b==r[0]:
                    for e in r[2]:
                        d={}
                        d=e
                      l1.append(int(d["Marks"]))
                      l2.append(d["Student Name"])
    plt.pie(l1,labels=l2)
    plt.show()


            
    
        
     
