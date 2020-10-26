def convertdate(date):
    months={
        'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
    }
    if '-' in date:
        return [int(x) for x in date.split('-')]
    elif '.' in date:
        return [int(x) for x in date.split('.')]
    elif '/' in date:
        return [int(x) for x in date.split('/')]
    else:
        date = date.split(' ')
        date[2]=int(date[2])
        date[1]=int(months[date[1][:3].lower()])
        date[0]=int(date[0][:-2])
        return date


monthslist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 
def countdays(d,m,y):
    total = y * 365 + d
    total+=sum(monthslist[:m-1])
    l = y - 1 if m<=2 else y
    total+=int(l//4-l//100+l//400)
    return total

with open("date_calculator.txt" , 'r') as rf:
    date1 = rf.readline().strip('\n')[6:]
    date2 = rf.readline().strip('\n')[6:]

date1=convertdate(date1)
date2=convertdate(date2)

ans = abs(countdays(date1[0],date1[1],date1[2])-countdays(date2[0],date2[1],date2[2]))
with open("output.txt",'w') as of:
    of.write("Date Differrence:%d Day"%(ans))



