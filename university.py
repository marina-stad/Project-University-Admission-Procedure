# write your code here
departments = (('Biotech', 2, 3), ('Chemistry', 3), ('Engineering', 4, 5), ('Mathematics', 4), ('Physics', 2, 4))
n = int(input())
students = []

with open('applicants.txt', 'r', encoding='utf-8') as f:
            for line in f:
                students += [line.split()]

students.sort()
dict_departments = dict()
#taken = sorted(students, )

#print('Successful applicants:')
#for i in taken[:m]:
#    print(*i[:2])


for i in departments:
#lambda x: True if x % 2 == 0 else False
    interim = sorted(filter(lambda x: x[7] == i[0], students), key=lambda x: max((int(x[i[1]]) + int(x[i[2]]))/2, int(x[6])) if len(i) > 2 else max(int(x[i[1]]), int(x[6])), reverse=True)
    if len(interim) >= n:
        dict_departments[i[0]] = interim[:n]
    else:
        dict_departments[i[0]] = interim[:len(interim)]

for i in dict_departments:
    for j in  dict_departments[i]:
        students.remove(j)

for k in range(8, 10):
    for i in departments:
        deficit = n - len(dict_departments[i[0]])
        if  deficit > 0:
            interim = sorted(filter(lambda x: x[k] == i[0], students), key=lambda x: max((int(x[i[1]]) + int(x[i[2]]))/2, int(x[6])) if len(i) > 2 else max(int(x[i[1]]), int(x[6])), reverse=True)
            if len(interim) >= deficit:
                dict_departments[i[0]].extend(interim[:deficit])
            else:
                dict_departments[i[0]].extend(interim[:len(interim)])

    for i in dict_departments:
        for j in  dict_departments[i]:
            if j in students:
                students.remove(j)

for i in departments:
    print(i[0])
    sort_dict_departments = sorted(dict_departments[i[0]])
    sort_dict_departments = sorted(sort_dict_departments, key=lambda x: max((int(x[i[1]]) + int(x[i[2]]))/2, int(x[6])) if len(i) > 2 else max(int(x[i[1]]), int(x[6])), reverse=True)

    with open(i[0].lower()+ '.txt', 'w', encoding='utf-8') as f:
        for j in  sort_dict_departments:
            if len(i) > 2:
                max_ball = max(round( ( int(j[i[1]]) + int(j[i[2]]) )/2, 1 ), int(j[6]) )
                line = j[0:2] +  [ str(max_ball) ]
                f.write(' '.join(line) + '\n')
            else:
                max_ball = max( int(j[i[1]]), int(j[6]))
                line = j[0:2] + [ str(max_ball) ]
                f.write(' '.join(line) + '\n')
