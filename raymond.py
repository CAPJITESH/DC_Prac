'''
This code simulates Raymond's Tree-Based Mutual Exclusion Algorithm for coordinating access to a 
Critical Section (CS) in a distributed system using a spanning tree.

🌳 Structure:
- Each process has a parent defined by the spanning tree (adjacency matrix).
- Only one process holds the token initially.
- If a process wants to enter CS, it sends a request to its parent.
- The token is passed down the tree toward the requesting process.

------------------------------------------------------------
🔢 Initialization:
- `n = 5`: Total 5 processes (IDs 0 to 4).
- `request_queue`: Stores pending requests for each process.
- `holder`: Shows from which process the current one expects to receive the token.
- `token`: Only the process with token=1 holds the permission to enter CS.
- `adj_matrix`: Represents the tree connections between processes.

------------------------------------------------------------
📥 User Input:
- User enters the process that wants to access the CS.

------------------------------------------------------------
🔄 find_parent(req_process) function:
- Called when a process wants to access the CS.
- Adds request to its own queue and sends a request to its parent.
- Recursively moves up the tree until a process is found that has the token.
- The parent that has the token will start the token-passing phase.

------------------------------------------------------------
🔁 Token Passing:
- While the requesting process does not have the token:
    - The process holding the token checks its queue.
    - Sends the token to the next requester in its queue.
    - Updates the `holder` and `token` accordingly.
    - This continues until the requester receives the token.

------------------------------------------------------------
✅ Entering Critical Section:
- Once the requesting process has the token and is first in its own queue:
    - It pops the request and enters the CS.
    - `holder` is updated to itself.

------------------------------------------------------------
🚪 Releasing the Critical Section:
- If no other pending requests in the request queue, CS is considered released.
- Final state of `holder` is printed showing updated holder links.

------------------------------------------------------------
📌 Key Points:
- Only one token exists in the system.
- Requests propagate up the tree to the token holder.
- Token is passed down the tree to the requester.
- The algorithm ensures fairness and avoids deadlock/starvation.
'''

'''
Simple Language

1. Start mein kya hai?
   - 5 processes hain (`0` to `4`).
   - Sirf ek process ke paas token hota hai (jo CS enter kar sakta hai).
   - Baaki processes ke paas nahi hota.
   - Sab processes tree (graph) structure mein connected hain (via `adj_matrix`).

2. Request karna (CS ke liye):
   - User se input lete hain ki kaunsa process CS mein enter karna chahta hai.
   - Wo process apne parent ko "request" bhejta hai.
   - Agar parent ke paas token nahi hai, toh wo aage apne parent ko request bhejta hai.
   - Ye tab tak chalta hai jab tak koi parent process milta hai jiske paas token ho.

3. Token pass karna:
   - Jis process ke paas token hai, wo apne request queue ke pehle wale process ko token bhejta hai.
   - Ye chain tab tak chalta hai jab tak token requested process tak nahi pahuch jaata.

4. Critical Section entry:
   - Jab requesting process ke paas token aa jaata hai aur wo request queue mein first hota hai,
     toh wo CS enter karta hai.
   - Request queue mein se khud ko hata deta hai.

5. Release karna CS:
   - Agar request queue empty ho jaati hai, toh process CS se bahar aa jaata hai.
   - System ready hota hai next request ke liye.

Important points
- Sirf ek token exist karta hai.
- Request upar jaata hai tree mein.
- Token neeche aata hai request karne wale tak.
- Deadlock aur starvation avoid kiya jaata hai.
- Sab kuch queue and holder ke through manage hota hai.

'''



n = 5

request_queue = {0: [], 1: [], 2: [], 3: [], 4: []}
holder = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1}
token = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0}

adj_matrix = [[1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0]]

print("Raymond Tree based Mutual Exclusion")
print("\nAdjacency Matrix for the spanning tree:\n")

for i in adj_matrix:
    print(*i)

req_process = int(input("\nEnter the process who wants to enter the CS: "))


def find_parent(req_process):
    request_queue[req_process].append(req_process)
    for i in range(n):
        if (adj_matrix[req_process][i] == 1):
            parent = i
            request_queue[parent].append(req_process)
            break

    print("\nProcess {} sending Request to parent Process {}".format(req_process, parent))
    print("\nRequest Queue:", request_queue)

    if (token[parent] == 1):
        return parent

    else:
        parent = find_parent(parent)

    return parent


parent = find_parent(req_process)

while (token[req_process] != 1):
    child = request_queue[parent][0]
    request_queue[parent].pop(0)
    holder[parent] = child
    holder[child] = 0
    token[parent] = 0
    token[child] = 1
    print("\nParent process {} has the token and sends the token to the reqeust process {}".format(parent, child))
    print("\nRequest Queue:", request_queue)
    parent = child

if (token[parent] == 1 and request_queue[parent][0] == parent):
    request_queue[parent].pop(0)
    holder[parent] = parent
    print("\nProcess {} enters the Critical Section".format(parent))
    print("\nRequest Queue:", request_queue)

if (len(request_queue[parent]) == 0):
    print("\nRequest queue of process {} is empty. Therefore Release Critical Section".format(parent))

print("\nHolder:", holder)