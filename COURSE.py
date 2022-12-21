import csv

crs=open("Course.csv","a+")
crsw=csv.writer(crs)
crsw.writerow(["Course ID","Course Name","Marks Obtained"])
crs.close()

def create_course():
    ans="y"
    while(ans=="y"):
        course_id=input("Enter Course ID:")
        course_name=input("Enter Course Name:")
        b=[]
        a="Y"
        while a=="Y":
            details=input("Enter StudentID of Student:")
            l=[]
        
            stu=open("Student.csv","r", newline="\r\n")
            stu.seek(0)
            stur=csv.reader(stu)
            for row in stur:
                if row[0]==details:
                    l.append(row[1])
                    l.append(row[2])
            stu.close()
            
            marks_obtained={}
            
        
            
            marks=input("Enter marks:")
            
            marks_obtained["Student Name"]=l[0]
            marks_obtained["Roll Number"]=l[1]
            marks_obtained["Marks"]=marks
            b.append(marks_obtained)
            a=input("Do you want to add more dictionaries?..........(Y/N)")
        crs=open("Course.csv","a")
        crsw=csv.writer(crs)
        crsw.writerow([course_id,course_name,b])
        crs.close()
        ans=input("Do you want to benter more data?.........(y/n)")

def view_performance():
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    for row in crsr:
        print(row[2])
    crs.close()

def view_histogram():
    c=open("Course.csv","r",newline="\r\n")
    c.seek(0)
    cr=csv.reader(c)
    f=False
    d={}
    l=[]
    for row in cr:
        if row[2]=="Marks Obtained":
            f=True
        else:
            for r in row[2]:
                d=r
                if d["Marks"]>=90:
                    l.append("A")
                elif d["Marks"]>=80:
                    l.append("B")
                elif d["Marks"]>=70:
                    l.append("C")
                elif d["Marks"]>=60:
                    l.append("D")
                elif d["Marks"]>=50:
                    l.append("E")
                elif d["Marks"]<40:
                    l.append("F")
                
    plt.hist(l)
    plt.xlabel("GRADES")
    plt.ylabel("NO.OF STUDENTS")
    plt.title("COURSE STATISTICS")
    plt.show()
    


