from copy import *
import random
import pickle
import time
from shutil import copyfile
global flag,obj,count,i

start_time=time.time()
ct=0
x_list=[]
y_list=[]
child_list=[]
rlist=[]
#################################################################
#class for inserting classes --eg:- semester 6 cse alpha,semester 8 cse alpha...etc. 
class day:
    def __init__(self,name):
        self.name=name
        self.monlist=monlist=[]
        self.tuelist=tuelist=[]
        self.wedlist=wedlist=[]
        self.thulist=thulist=[]
        self.frilist=frilist=[]
    def op1(self,a):
        self.monlist.append(a)
    def op2(self,a):
        self.tuelist.append(a)
    def op3(self,a):
        self.wedlist.append(a)
    def op4(self,a):
        self.thulist.append(a)
    def op5(self,a):
        self.frilist.append(a)
            
class deprt:
    def __init__(self,name):
        self.name=name
        self.tlist=tlist=[]
        self.sublist=sublist=[]
        self.codelist=codelist=[]
        self.lablist=lablist=[]
        self.labcodelist=labcodelist=[]
        
    def fn(self,tlist,codelist,sublist):
        self.tlist.append(tlist)
        self.sublist.append(sublist)
        self.codelist.append(codelist)
        
    def lab(self,lablist,labcodelist):
        self.lablist.append(lablist)
        self.labcodelist.append(labcodelist)
        
def trun(t):
    ch=''
    for i in t:
        if i!='\n':
            ch=ch+i
        else:
            return ch
#Generation of time tables -- such that no teachers will have hours in different classes at the same time
#Each day will have 7 hours
def generate():
    tmp=0
    cnt=0
    for item in obj:
        dup=[]
        t=day(item.name)
        if cnt == 0:
            m=0
            while m < 7:
                a=random.choice(item.tlist)
                t.op1(a)
                a=random.choice(item.tlist)
                t.op2(a)
                a=random.choice(item.tlist)
                t.op3(a)
                a=random.choice(item.tlist)
                t.op4(a)
                a=random.choice(item.tlist)
                t.op5(a)
                m=m+1
            table.append(t)
            cnt=1
            temp=cnt
        else:
            while cnt > 0:
                cnt=cnt-1
                dup.append(table[cnt])
            m=0
            fg=0
            while m < 7:
                fg=0
                a=random.choice(item.tlist)
                for var in dup:
                    if var.monlist[m] == a:
                        fg=1
                if fg == 0:
                    m=m+1
                    t.op1(a)
            m=0
            fg=0
            while m < 7:
                fg=0
                a=random.choice(item.tlist)
                for var in dup:
                    if var.tuelist[m] == a:
                        fg=1
                if fg == 0:
                    m=m+1
                    t.op2(a)
            m=0
            fg=0
            while m < 7:
                fg=0
                a=random.choice(item.tlist)
                for var in dup:
                    if var.wedlist[m] == a:
                        fg=1
                if fg == 0:
                    m=m+1
                    t.op3(a)
            m=0
            fg=0
            while m < 7:
                fg=0
                a=random.choice(item.tlist)
                for var in dup:
                    if var.thulist[m] == a:
                        fg=1
                if fg == 0:
                    m=m+1
                    t.op4(a)
            m=0
            fg=0
            while m < 7:
                fg=0
                a=random.choice(item.tlist)
                for var in dup:
                    if var.frilist[m] == a:
                        fg=1
                if fg == 0:
                    m=m+1
                    t.op5(a)
            table.append(t)
            cnt=temp
            cnt=cnt+1


########################ga#############################################################################################
################ Fitness function --this function checks and returns the overall fitness score of a given timetable 
def fitness():
    global ct
    objlist=copy(child_list)
    list=[]
    f = open("constraints.txt","rb")
    list=pickle.load(f)
    f.close()
    count=list[0]
    ct=count
    count+=1
    del list[0]
    bt=0
    for item in child_list:
        for back in child_list:
            if back.name == item.name:
                continue
            hour=0
            flg=0
            flg2=0
            while hour < 7:
                if item.monlist[hour] == back.monlist[hour]:
                    bt=1
                    flg=1
                    break
                if item.tuelist[hour] == back.tuelist[hour]:
                    bt=1
                    flg=1
                    break
                if item.wedlist[hour] == back.wedlist[hour]:
                    bt=1
                    flg=1
                    break
                if item.thulist[hour] == back.thulist[hour]:
                    bt=1
                    flg=1
                    break
                if item.frilist[hour] == back.frilist[hour]:
                    bt=1
                    flg=1
                    break
                hour=hour+1
            if flg==1:
                flg2=1
                break
        if flg2 == 1:
            count-=1
            break
    
 ####################################################################   
    if list[0]==1:
        flag1=0
        for item in objlist:
            if item.frilist[3] == 'Ms. Shimmi Asokan':
                flag1 = 1
        if flag1==1:
            count-=1
    if list[1]==1:
        flag2=0
        libcount=0
        for item in objlist:
            if 'lib' in item.monlist:
                libcount+=1
                if libcount > 1:
                    flag2 = 1
            if 'lib' in item.tuelist:
                libcount+=1
                if libcount > 1:
                    flag2 = 1
            if 'lib' in item.wedlist:
                libcount+=1
                if libcount > 1:
                    flag2 = 1
            if 'lib' in item.thulist:
                libcount+=1
                if libcount > 1:
                    flag2 = 1
            if 'lib' in item.frilist:
                libcount+=1
                if libcount > 1:
                    flag2 = 1
        if flag2==1:
            count-=1
    if list[2]==1:
        flag3=0
        for item in objlist:
            for i in range(0, 7):
                hourcount = 0
                if item.monlist[i] != 'lib':
                    for j in range(0, 7):
                        if item.monlist[i] == item.monlist[j]:
                            hourcount = hourcount + 1
                            if hourcount > 2:
                                flag3 = 1
            for i in range(0, 7):
                hourcount = 0
                if item.tuelist[i] != 'lib':
                    for j in range(0, 7):
                        if item.tuelist[i] == item.tuelist[j]:
                            hourcount = hourcount + 1
                            if hourcount > 2:
                                flag3 = 1
            for i in range(0, 7):
                hourcount = 0
                if item.wedlist[i] != 'lib':
                    for j in range(0, 7):
                        if item.wedlist[i] == item.wedlist[j]:
                            hourcount = hourcount + 1
                            if hourcount > 2:
                                flag3 = 1
            for i in range(0, 7):
                hourcount = 0
                if item.thulist[i] != 'lib':
                    for j in range(0, 7):
                        if item.thulist[i] == item.thulist[j]:
                            hourcount = hourcount + 1
                            if hourcount > 2:
                                flag3 = 1
            for i in range(0, 7):
                hourcount = 0
                if item.frilist[i] != 'lib':
                    for j in range(0, 7):
                        if item.frilist[i] == item.frilist[j]:
                            hourcount = hourcount + 1
                            if hourcount > 2:
                                flag3 = 1
    
        if flag3==1:
            count-=1
    
        
    
    return count
####################################################################################################
##### pop function --this function is used to insert the time table having best fitness into a file
def pop(fit,gen):
    rlist=[]
    for item in names:
        a=''
        a=item+".txt"
        item=open(a,'ab')
        rlist.append(item)
    for item in child_list:
        m=0
        for item1 in rlist:
            if item1.name == names[m]:
                break
            pickle.dump(item.monlist,item1)
            pickle.dump(item.tuelist,item1)
            pickle.dump(item.wedlist,item1)
            pickle.dump(item.thulist,item1)
            pickle.dump(item.frilist,item1)
            m=m+1 
    for item in rlist:
        item.close()
        
        
        
    
#################################################################################################################################################
##############shuffle function -- this function is used to shuffle the time tables in the file where the time tables with best fitness are stored
def shuffle():
    rlist=[]
    pool=[]
    for item in names:
        a=''
        a=item+".txt"
        item=open(a,'rb')
        rlist.append(item)
        i=0
        for item in rlist:

            while 1:
                try:
                    p=day(names[i])
                    a=pickle.load(item)
                    for data in a:
                        p.op1(data)
                    a=pickle.load(item)
                    for data in a:
                        p.op2(data)
                    a=pickle.load(item)
                    for data in a:
                        p.op3(data)
                    a=pickle.load(item)
                    for data in a:
                        p.op4(data)
                    a=pickle.load(item)
                    for data in a:
                        p.op5(data)
                    pool.append(p)
                except:
                    break
            i=i+1
############complete shuffle#################
    random.shuffle(pool)
#############################################
    for item in rlist:
        item.close()
    rlist=[]
    for item in names:
        a=item+".txt"
        item=open(a,'wb')
        rlist.append(item)
    i=0
    for item in rlist:
        name=names[i]
        for atom in pool:
            if atom.name == name:
                pickle.dump(atom.monlist,item)
                pickle.dump(atom.tuelist,item)
                pickle.dump(atom.wedlist,item)
                pickle.dump(atom.thulist,item)
                pickle.dump(atom.frilist,item)
        i=i+1
        
    for item in rlist:
        item.close()
    
            
        
    
    

#############selection --to select two parent time tables from the pool
def selection():
    global x_list,y_list,child_list,rlist
    rlist=[]
    for item in names:
        a=''
        a=item+".txt"
        item=open(a,'rb')
        rlist.append(item)
    child_list=[]
    x_list=[]
    i=0
    for item in rlist:
        p=day(names[i])
        a=pickle.load(item)
        p.op1(a)
        a=pickle.load(item)
        p.op2(a)
        a=pickle.load(item)
        p.op3(a)
        a=pickle.load(item)
        p.op4(a)
        a=pickle.load(item)
        p.op5(a)
        i=i+1
        x_list.append(p)
    y_list=[]
    i=0
    for item in rlist:
        p=day(names[i])
        a=pickle.load(item)
        p.op1(a)
        a=pickle.load(item)
        p.op2(a)
        a=pickle.load(item)
        p.op3(a)
        a=pickle.load(item)
        p.op4(a)
        a=pickle.load(item)
        p.op5(a)
        y_list.append(p)
        i=i+1
    for item in rlist:
        item.close()

##############crossover#############################################################
def crossover():
    global child_list
    re=0
    lib=[0,1]
    child_list=[]
    randu=[0,1,2,3,4,5,6]
    m=-1
    for item1 in x_list:
        m=m+1
        d=day(item1.name)
        for item2 in y_list:
            if d.name == item2.name:
                d.name=item1.name
                i=0
                while i < 5:
                    ch=random.choice(lib)
                    if ch == 0:
                        if i == 0:
                            for a in item1.monlist[0]:
                                d.op1(a)
                        if i == 1:
                            for a in item1.tuelist[0]:
                                d.op2(a)
                        if i == 2:
                            for a in item1.wedlist[0]:
                                d.op3(a)
                        if i == 3:
                            for a in item1.thulist[0]:
                                d.op4(a)
                        if i == 4:
                            for a in item1.frilist[0]:
                                d.op5(a)
                    if ch == 1:
                        if i == 0:
                            for a in item1.monlist[0]:
                                d.op1(a)
                        if i == 1:
                            for a in item1.tuelist[0]:
                                d.op2(a)
                        if i == 2:
                            for a in item1.wedlist[0]:
                                d.op3(a)
                        if i == 3:
                            for a in item1.thulist[0]:
                                d.op4(a)
                        if i == 4:
                            for a in item1.frilist[0]:
                                d.op5(a)
                    i=i+1
                child_list.append(d)

##############mutation##############################################################
def mutation():
    i=0
    for item1 in child_list:
        name=names[i]
        for item2 in obj:
            if item1.name == item2.name:
                ch=random.choice(item2.tlist)
                a=random.randint(0,6)
                item1.monlist[a]=ch
                ch=random.choice(item2.tlist)
                a=random.randint(0,6)
                item1.tuelist[a]=ch
                ch=random.choice(item2.tlist)
                a=random.randint(0,6)
                item1.wedlist[a]=ch
                ch=random.choice(item2.tlist)
                a=random.randint(0,6)
                item1.thulist[a]=ch
                ch=random.choice(item2.tlist)
                a=random.randint(0,6)
                item1.frilist[a]=ch
        i+=1

############################################################################### 
#main()
list=[]
f = open("constraints.txt","rb")
list=pickle.load(f)
f.close()
gen=list[0]
names=[]
count=0
obj=[]
table=[]
ch=''
t=''
code=''
sub=''
lab=''
k=0
allsub=[]
fp=open("input.txt",'r')
allsub=fp.readlines()
i=0
##########Read from the input file (the input file is created by MainGUI.py from the excel sheet)
while 1:
    flag=0
    ch=trun(allsub[i])
    if ch in names:
        ch=ch
    else:
        names.append(ch)
        
    if i == 0:
        j=deprt(ch)
        i=i+1
        t=trun(allsub[i])
        i=i+1
        code=trun(allsub[i])
        i=i+1
        sub=trun(allsub[i])
        if sub != 'lab':
            j.fn(t,code,sub)
            i=i+2
            if allsub[i]=='end':
                break
        else:
            j.lab(t,code)
            i=i+1
            if allsub[i] == 'end':
                break
        obj.append(j)
        flag=1
    else:
        for item in obj:
            if ch == item.name:
                flag=1
                i=i+1
                t=trun(allsub[i])
                i=i+1
                code=trun(allsub[i])
                i=i+1
                sub=trun(allsub[i])
                if sub != 'lab':
                    item.tlist.append(t)
                    item.codelist.append(code)
                    item.sublist.append(sub)
                    i=i+2
                    if allsub[i]=='end':
                        break
                else:
                    item.lablist.append(t)
                    item.labcodelist.append(code)
                    i=i+1
                    if allsub[i] == 'end':
                        break
                break
            
        if flag == 0:
            if allsub[i] == 'end':
                break
            j=deprt(ch)
            i=i+1
            t=trun(allsub[i])
            i=i+1
            code=trun(allsub[i])
            i=i+1
            sub=trun(allsub[i])
            if sub != 'lab':
                j.fn(t,code,sub)
                i=i+2
                if allsub[i]=='end':
                    break
            else:
                j.lab(t,code)
                i=i+1
                if allsub[i] == 'end':
                    break
            obj.append(j)
names.pop()
pointerlist=[]
lablist=[]
for item in names:
    a=''
    a=item+".txt"
    item=open(a,'wb')
    pointerlist.append(item)
for item in names:
    a=''
    a=item+"lab.txt"
    item=open(a,'w')
    lablist.append(item)
    
i=0
while i<50:
    table=[]
    generate()
    loopvar=-1
    for item in pointerlist:
        m=0
        loopvar=loopvar+1
        for var in table:
            if m < loopvar:
                m=m+1
                continue
            else:
                break
        pickle.dump(var.monlist,item)
        pickle.dump(var.tuelist,item)
        pickle.dump(var.wedlist,item)
        pickle.dump(var.thulist,item)
        pickle.dump(var.frilist,item)
    i=i+1
loopvar=-1
for item in lablist:
        m=0
        loopvar=loopvar+1
        for var in obj:
            if m < loopvar:
                m=m+1
                continue
            else:
                break
        for k in var.lablist:
            item.write("%s "%k)
for item in pointerlist:
    item.close()
for item in lablist:
    item.close()
fp=open("total_no_room.txt","wb")
for item in names:
    pickle.dump(item,fp)
fp.close()
#####################GA################################
re=0
generation=0
ft=-1
prefit=0
pre=0
print(gen+1)
while ft!=gen+1:
    selection()
    crossover()
    mutation()
    ft=fitness()
    if pre < ft:
        pre=copy(ft)
        pop(ft,generation)
    shuffle()
    generation=generation+1
    print("generation=",generation,"fitness=",ft)
    a=open("johny.txt",'wb')
for item in child_list:
    print("hit")
    print(item.name)
    pickle.dump(item.name,a)
    pickle.dump(item.monlist,a)
    pickle.dump(item.tuelist,a)
    pickle.dump(item.wedlist,a)
    pickle.dump(item.thulist,a)
    pickle.dump(item.frilist,a)
    print(item.monlist)
    print(item.tuelist)
    print(item.wedlist)
    print(item.thulist)
    print(item.frilist)
    print()
print("Time for completion :"+str(time.time()-start_time)+" seconds")
a.close()
a=open("time.txt",'wb')
pickle.dump(str(time.time()-start_time),a)
a.close()

    
    
          

















