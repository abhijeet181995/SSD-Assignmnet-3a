import json
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

def output(free1,free2,duration,d,ans):
    with open("output.txt",'w') as of:
        of.write("Employee1:")
        of.write(json.dumps(convertfinallist(free1)))
        of.write("\nEmployee2:")
        of.write(json.dumps(convertfinallist(free2)))
        of.write("\nSlot Duration:%.1f hrs \n"%(duration))
        if len(ans)==0:
            of.write(json.dumps({d:"No Available slots"}))
        else:
            of.write(json.dumps({d:convertfinallist(ans)}))


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

with open("Employee1.txt" , 'r') as e1:
    dic1 = eval(e1.read())

with open("Employee2.txt" , 'r') as e2:
    dic2 = eval(e2.read())

if dic1['Employee1'].keys()==dic2['Employee2'].keys():
    d = list(dic1['Employee1'].keys())[0]
    free1 = process_slots(dic1['Employee1'][d])
    free2 = process_slots(dic2['Employee2'][d])
    free3 = [x for x in free1 if x in free2]
    ans=[]
    slotduration = float(input("Input The Slot Duration\n"))
    slotdurationmins = int(slotduration*60)
    for slot in combine(free3):
        if alltimeslot.index(slot[0])+slotdurationmins<len(alltimeslot):
            if alltimeslot[(alltimeslot.index(slot[0])+slotdurationmins)] <= slot[1]:
                ans.append([slot[0],alltimeslot[(alltimeslot.index(slot[0])+slotdurationmins)]])
                break
    output(combine(free1),combine(free2),slotduration,d,ans)
else:
    print("No Slot Available")