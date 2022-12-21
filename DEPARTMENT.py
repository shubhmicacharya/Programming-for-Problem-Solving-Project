import csv
import matplotlib.pyplot as plt
dept=open("Department.csv","a+")
deptw=csv.writer(dept)
deptw.writerow(["Department ID","Department Name","List of Batches"])
dept.close()

def create_department():
    ans="y"
    while ans=="y":
        dep_id=input("Enter Department ID:")
        dep_name=input("Enter Department Name:")
        l=[]
        a="Y"
        while a=="Y":
            n=input("Enter BatchID:")
            l.append(n)
            a=input("Do you want to enter more batches?..........(Y/N)")
        dept=open("Department","a+")
        deptw=csv.writer(dept)
        deptw.writerow([dep_id,dep_name,l])
        dept.close()
        print("Your data as follows:")
        dept=open("Department","a+")
        dept.seek(0)
        deptr=csv.reader(dept)
        for row in deptr:
            print(row)
        dept.close()

def view_batch():
     dept=open("Department.csv","a+")
     dept.seek(0)
     found=False
     deptr=csv.reader(dept)
     for row in deptr:
         if row[2]=="List of Batches":
             found=True
         else:
             print(row[2])
     dept.close()

def avg_performance():
    dept=open("Department.csv","r",newline="\r\n")
    dept.seek(0)
    deptr=csv.reader(dept)
    l=[]
    for row in deptr:
        l=l+row[2]
    dept.close()
    batch=open("Batch.csv","r",newline="\r\n")
    batch.seek(0)
    batchr=csv.reader(batch)
    lt=[]
    for r in l:
        for b in batchr:
            if b[0]==r:
                lt.append(b[3])
    batch.close()
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    x={}
    for n in lt:
        for c in crsr:
            if c[0]==n:
                x=crsr[2]
                print(n,x["Marks"])
    crs.close()
def line_plot():
    dep=open("Department.csv","r",newline="\r\n")
    dep.seek(0)
    depr=csv.reader(dep)
    l=[]
    l2=[]
    for row in depr:
        for r in row[2]:
            l.append(r)
    dep.close()
    ba=open("Batch.csv","r",newline="\r\n")
    ba.seek(0)
    bar=csv.reader(ba)
    f=False
    for roww in bar:
        if roww[0]=="Batch ID":
            f=True
        else:
            for rw in l:
                if rw==roww[0]:
                l1=[]
                    for a in roww[3]:
                        l1.append(a)
                    l2.append(l1)
    ba.close()
    l3=[]
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    for row1 in crsr:
        for r1 in l2:
            d=0.0
            k=0
            for bb in r1:
                a=0
                c=0
                if row1[0]==bb:
                    for cc in row1[2]:
                        a+=int(cc["Marks"])
                        c+=1
                    d+=a/c
                k+=1
            l3.append(d/k)
    crs.close()
    plt.plot(l2,l3)
    plt.show()
