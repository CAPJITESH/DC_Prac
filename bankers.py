'''
1. Take number of processes and resources  
   - User inputs number of processes (`p`) and number of resource types (`r`).

2. Input total instances for each resource type  
   - User enters how many total instances of each resource type are available in the system.

3. Input Max matrix  
   - For each process, input its maximum demand for each resource type.
   - `max[i][j]` means process `i` may require at most `j` units of resource type `j`.

4. Input Allocation matrix  
   - For each process, input how many resources are currently allocated to it.
   - `alloc[i][j]` means process `i` is currently holding `j` units of resource `j`.

5. Calculate total allocated resources (sum)  
   - Add up the total allocated units of each resource.

6. Calculate Available resources  
   - `avail[j] = instances[j] - sum[j]`
   - Shows what’s left with the system.

7. Calculate Need matrix  
   - `need[i][j] = max[i][j] - alloc[i][j]`
   - How much more a process may still need to complete.

8. Find Safe Sequence using Banker's Algorithm  
   - Repeatedly find a process whose `need <= avail`.
   - If found, add it to the `safeSequence`, release its resources to `avail`, and mark it completed.
   - Repeat until all processes are done or no eligible process is found.

9. Check if system is safe  
   - If all processes complete → safe state, print sequence.
   - Else → unsafe state, deadlock possibility.

'''

p = int(input("Enter the no. of processes: "))
r = int(input("Enter the no. of resources: "))

instances = []
print()
for i in range(r):
  instance = int(input("Enter the instances of resource type R{}: ".format(i+1)))
  instances.append(instance)

max = []
print("\nEnter the Max matrix for each process:")
for i in range(p):
  max_i = [int(item) for item in input("P{}: ".format(i+1)).split()]
  max.append(max_i)

alloc = []
print("\nEnter the Allocated matrix for each process:")
for i in range(p):
  alloc_i = [int(item) for item in input("P{}: ".format(i+1)).split()]
  alloc.append(alloc_i)

completed = []
for i in range(p):
    completed.append(0)

sum = []
for i in range(r):
    sum.append(0)

for i in range(p):
    for j in range(r):
        sum[j] += alloc[i][j]

avail = []
for i in range(r):
    avail.append(instances[i] - sum[i])

need = []
print("\nNeed matrix: ")
for i in range(p):
    need_i = []
    print("P{}: ".format(i + 1), end="")
    for j in range(r):
        print(max[i][j] - alloc[i][j], end=" ")
        need_i.append(max[i][j] - alloc[i][j])
    print()
    need.append(need_i)

count = 0
safeSequence = []
start = 0

while True:
    process = -1
    for i in range(start, p):
        if completed[i] == 0:
            process = i
            for j in range(r):
                if (avail[j] < need[i][j]):
                    process = -1
                    break

        if process != -1:
            break

    if process != -1:
        safeSequence.append(process + 1)
        count += 1
        for j in range(r):
            avail[j] += alloc[process][j]
            alloc[process][j] = 0
            max[process][j] = 0
            completed[process] = 1

    if count != p and process != -1:
        if (process + 1 == p):
            start = 0
        else:
            start = process + 1
        continue
    else:
        break

if (count == p):
    print("\nThe system is in a Safe State.")
    print("Safe Sequence : < ", end="")
    for i in range(p):
        print("P{}".format(safeSequence[i]), end=" ")
    print(">")
else:
    print("\nThe system is in an Unsafe State.")