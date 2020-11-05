import json
import os
def convertfinallist(free):
    finallist=[]
    flag0=0
    flag1=0
    for slot in free:
        if slot[0]>=1300:
            slot[0]=slot[0]-1200
            flag0=1
        if slot[1]>=1300:
            slot[1]=slot[1]-1200
            flag1=1
        slot[0]=list(str(slot[0]))
        slot[1]=list(str(slot[1]))
        slot[0].insert(-2,':')
        if flag0:
            slot[0]+="PM"
        else:
            slot[0]+="AM"
        slot[1].insert(-2,':')
        if flag1:
            slot[1]+="PM"
        else:
            slot[1]+="AM"
        slot[0]=''.join(slot[0])
        slot[1]=''.join(slot[1])
        finallist.append(slot[0]+'-'+slot[1])
    return finallist

def output(employee_names,list_free,duration,date,ans):
    with open("output.txt",'w') as of:
        for i in range(len(employee_names)):
            of.write(employee_names[i])
            of.write(":")
            of.write(json.dumps(convertfinallist(list_free[i])))
            of.write("\n")
        of.write("\nSlot Duration:%.1f hrs \n"%(duration))
        if len(ans)==0:
            of.write(json.dumps({date:"No Available slots"}))
        else:
            of.write(json.dumps({date:convertfinallist(ans)}))


def genratelist(start,end):
    common=[]
    for x in range(start,end):
        if x%100>59:
            continue
        else:
            common.append(x)
    return common

def combine(slots):
    ans=[]
    start=slots[0]
    prev=slots[0]
    for next in slots[1:]:
        if next==prev+1:
            prev=next
        elif prev%100==59 and prev//100+1==next//100:
            prev=next
        else:
            if start!=prev:
                ans.append([start,prev])
            start=next
            prev=next
    if start!=prev:
        ans.append([start,prev])
    return ans
                

def process_slots(slotss):
    lst=[]
    for slots in slotss:
        start , end = slots.split('-')
        start=int(start.strip(' ').replace(':','')[:-2])
        end=int(end.strip(' ').replace(':','')[:-2])
        if start < 900:
            start +=1200
        if end < 900:
            end +=1200
        lst+=genratelist(start+1,end)
    freeslots=[x for x in alltimeslot if x not in lst]
    return freeslots

       
alltimeslot=genratelist(900,1701)

list_files = os.listdir("Employee")
list_files_path = ["Employee/"+x for x in list_files]
list_dic=[]

for file in list_files_path:
    with open(file , 'r') as e1:
        dic = eval(e1.read())
        list_dic.append(dic)


employee_names = [x[:-4] for x in list_files]

flag=0

date1  = list(list_dic[0][employee_names[0]].keys())[0]
date2 = list(list_dic[1][employee_names[1]].keys())[0]

if date1!=date2:
    flag=1

free1 = process_slots(list_dic[0][employee_names[0]][date1])
free2 = process_slots(list_dic[1][employee_names[1]][date2])
free3 = [x for x in free1 if x in free2]

list_free =[]
list_free.append(combine(free1))
list_free.append(combine(free2))


for i in range(2,len(employee_names)):
    currdate=list(list_dic[i][employee_names[i]].keys())[0]
    if currdate!=date1:
        flag=1
    free = process_slots(list_dic[i][employee_names[i]][currdate])
    list_free.append(combine(free))
    free3 = [x for x in free if x in free3]

ans=[]
slotduration = float(input("Input The Slot Duration\n"))
slotdurationmins = int(slotduration*60)
for slot in combine(free3):
    if alltimeslot.index(slot[0])+slotdurationmins<len(alltimeslot):
        if alltimeslot[(alltimeslot.index(slot[0])+slotdurationmins)] <= slot[1]:
            ans.append([slot[0],alltimeslot[(alltimeslot.index(slot[0])+slotdurationmins)]])
            break

if flag==1:
    ans=[]
    output(employee_names,list_free,slotduration,date1,ans)
else:
    output(employee_names,list_free,slotduration,date1,ans)
