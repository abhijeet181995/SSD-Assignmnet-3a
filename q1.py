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



input_list= [x for x in input().split(' ')]
parent_list =[]
for emp in input_list[1:]:
    parent=[]
    while graph[emp]!="Not Available":
        parent.append(graph[emp])
        emp = graph[emp]
    parent_list.append(parent)




common = [ans for ans in parent_list[0] if ans in parent_list[1]]
for parent in parent_list[2:]:
    common = [ans for ans in parent if ans in common]

# print(common)

if len(common)==0:
    print("Not Available")
else:
    print(common[0])
    for emp in input_list[1:]:
        print(common[0],"is %d levels above %s"%((level[emp]-level[common[0]]),emp))

