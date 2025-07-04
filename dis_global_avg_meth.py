'''
1. Required modules import karo  
2. Time ko timedelta mein convert karne ka function banao  
3. User se agreed time aur sab machines ke current time ka input lo  
4. Har machine ka skew calculate karo (agreed time se kitna difference hai)  
5. Skew values ko store karo aur table print karo  
6. 5 minute ke interval mein sab machines ka time badhao (simulate karo)  
7. Har round ke baad skew fir se calculate karo aur table print karo  
8. Sab machines ka average skew calculate karo (jitne rounds chale utne ka average)  
9. Agar average skew positive hai toh machine ka time ghatao, negative hai toh badhao  
10. Final adjusted time print karo for synchronization
'''
from datetime import timedelta

num = {'00':0,'01':1,'02':2,'03':3,'04':4,'05':5,'06':6,'07':7,'08':8,'09':9}

curr_time = {}
skewdct = {}

machines = ['Machine']
curr_time_lst = ['Current Time']
skew_lst = ['Skew']

def calTime(time):
    a,b = time.split(':')
    if b in num:
        b = num[b]
    secs = int(a)*60*60 + int(b)*60
    td = timedelta(seconds=secs)
    return td

def calcSkew():
    for t in curr_time:
        diff = curr_time[t] - ag_time
        diff_in_min = int(diff.total_seconds()/60)
        skewdct[t].append(diff_in_min)
        skew_lst.append(diff_in_min)

        if ag_time == curr_time[t]:
            print("\nMessage sent by Machine {}".format(t))

def calcSync(avg,m):
    abs_avg = abs(avg)
    print('Current Time of Machine {}: {}'.format(m,curr_time[m]))

    if avg > 0:
        new_time = curr_time[m] - timedelta(minutes=abs_avg)
        print('Hence decreases its clock by {} to get time:{} '.format(abs_avg, str(new_time)))
    else:
        new_time = curr_time[m] + timedelta(minutes=abs_avg)
        print('Hence increases its clock by {} to get time:{} '.format(abs_avg, str(new_time)))

def printTable():
    print("\n" + "-" * 50)
    for i in range(len(machines)):
        print(f"{str(machines[i]):<10} | {str(curr_time_lst[i]):<20} | {str(skew_lst[i]):<10}")
    print("-" * 50)

ag_time = input("Enter Agreed Upon Time: ")
n = int(input("Enter no. of machines: "))
time_lst = [x for x in input("Enter current time of {} Machines: ".format(n)).split()]

ag_time = calTime(ag_time)

for i in range(0,n):
    curr_time[i+1] = calTime(time_lst[i])
    curr_time_lst.append(curr_time[i+1])
    skewdct[i+1] = []
    machines.append(i+1)

print('\nAgreed Upon Time: ',str(ag_time))
calcSkew()
printTable()

counter = 1

while counter != n:
    print("\nAfter 5 mins:")
    curr_time_lst = ['Current Time']
    skew_lst = ['Skew']

    for t in curr_time:
        curr_time[t] += timedelta(minutes=5)
        curr_time_lst.append(curr_time[t])

    calcSkew()
    printTable()

    counter+=1

for i in skewdct:
    s=0
    for skew in skewdct[i]:
        s += skew
    avg = s/n
    print("\nSkew of Machine {} is {}".format(i,avg))
    calcSync(avg,i)
