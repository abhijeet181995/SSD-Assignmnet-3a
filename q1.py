with open('org.json', 'r') as rfile:
    dic = eval(rfile.read())

graph={}
level={}
for k in dic.keys():
    for ind in range(len(dic[k])):
        if k=="L0":
            graph[dic[k][ind]['name']]="Not Available"
            level[dic[k][ind]['name']]=0
        else:
            graph[dic[k][ind]['name']]=dic[k][ind]['parent']
            level[dic[k][ind]['name']]=int(k[1])

emp1,emp2= [x for x in input().split(' ')]
cemp1=emp1
cemp2=emp2
parent1 = []
parent2 = []

while graph[emp1]!="Not Available":
    parent1.append(graph[emp1])
    emp1 = graph[emp1]

while graph[emp2]!="Not Available":
    parent2.append(graph[emp2])
    emp2 = graph[emp2]

common = [ans for ans in parent1 if ans in parent2]
if len(common)==0:
    print("Not Available")
else:
    print(common[0])
    print(common[0],"is %d levels above %s"%((level[cemp1]-level[common[0]]),cemp1))
    print(common[0],"is %d levels above %s"%((level[cemp2]-level[common[0]]),cemp2))

