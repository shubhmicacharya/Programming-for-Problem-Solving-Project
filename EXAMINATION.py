import csv
import matplotlib.pyplot as plt
ex=open("Examination","a")
exw=csv.writer(ex)
exw.writerow(["marks","Course name","Roll no."])
ex.close()
def markss():
    a="y"
    while a=="y":
        m=input("enter marks:")
        c=input("enter course name:")
        r=input("enter roll number:")
        ex=open("Examination","a")
        exw=csv.writer(ex)
        exw.writerow([m,c,r])
        ex.close()
        a=input("do you want to input more data?........(y/n)")

def pf():
    ex=open("Examination","r",newline="\r\n")
    ex.seek(0)
    exr=csv.reader(ex)
    f=False
    for row in exr:
        if row[0]=="marks":
            f=True
        else:
            print(row)
            if int(row[0])>=90:
                print("A","PASS")
            elif int(row[0])>=80:
                print("B","PASS")
            elif int(row[0])>=70:
                print("C","PASS")
            elif int(row[0])>=60:
                print("D","PASS")
            elif int(row[0])>=50:
                print("E","PASS")
            elif int(row[0])<40:
                print("F","FAIL")
    ex.close()
def scatter_plot():
    ba=open("Batch.csv","r",newline="\r\n")
    ba.seek(0)
    bar=csv.reader(ba)
    f=False
    l=[]
    l2=[]
    for roww in bar:
        if roww[0]=="Batch ID":
            f=True
        else:
            l1=[]
            l.append(roww[0])
            for r in roww[3]:
                l1.append(r)
            l2.append(l1)

    ba.close()
    l3=[]
    crs=open("Course.csv","r",newline="\r\n")
    crs.seek(0)
    crsr=csv.reader(crs)
    for row1 in crsr:
        for r1 in l2:
            
            for bb in r1:
                l4=[]
                if row1[0]==bb:
                    for cc in row1[2]:
                        l4.append(int(cc["Marks"]))
            l3.append(l4)
    crs.close()
    plt.scatter(l3,l)
    plt.show()

