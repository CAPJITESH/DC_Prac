'''
1. Processes ka Setup  
   - `num` processes lete hain.
   - Sabko initially "alive" maana jaata hai (sabke clocks chal rahe hain).

2. Ek Process ko Crash karna  
   - User se input lete hain ki kaunsa process crash ho gaya (fail ho gaya).
   - Us process ko inactive (False) mark kar dete hain.

3. Election Start Karna  
   - Ek process (jo alive hai) election start karta hai.
   - Is process ko "initiator" bolte hain.

4. Election Message bhejna  
   - Initiator process sabse bade (higher ID) processes ko message bhejta hai: "Election".
   - Jo higher process alive hai, vo reply karta hai: "Okay", aur khud election start karta hai.

5. Recursive Election Handling  
   - Jab higher process Okay bhejta hai, to vo khud election message aage bhejta hai.
   - Yeh process tab tak chalta hai jab tak koi aur higher process alive na ho.

6. Coordinator Declaration  
   - Jo sabse bada alive process hai, wahi coordinator ban jaata hai.
   - Vo sabhi alive processes ko message bhejta hai: "Main Coordinator hoon".


Real-world Analogy:
Socho ek group hai jisme sab logon ke paas unique IDs hain. Agar leader chala jaata hai, to chhoti ID waala banda bolta hai “bhaiyo leader nahi raha, naye leader ki chahiye!”. Fir bada ID waala aake bolta hai “main hoon bada, main election chalu karta hoon” – aur sabse bada jo rehta hai, woh leader ban jaata hai.

'''
no_of_machines = int(input("Enter no. of machines: "))
detect_machine = int(input("Enter machine who sends a message: "))
down_machine = int(
    input("Enter machine who does not respond to Machine {} within time interval T: ".format(detect_machine)))

high_priority_machines = []

for i in range(detect_machine + 1, no_of_machines + 1):
    if (i != down_machine):
        high_priority_machines.append(i)

print()

print("Machine {} sending Election Message to Machines ---->".format(detect_machine), end=" ")
for i in high_priority_machines:
    print(i, end=" ")

print("\n")

repsonse_high_priority_machines = {}

l = len(high_priority_machines)
c = 0
for i in range(0, l):
    c += 1
    print("Machine {} responding OK to the Election Message".format(high_priority_machines[i]))

print("\nNo of machines responded OK to Election Message:", c)

while (len(high_priority_machines) != 1):
    c = 0
    sender = high_priority_machines[0]
    l = len(high_priority_machines)
    print("\nMachine {} sending Election Message to Machines ---->".format(sender), end=" ")
    for i in range(1, l):
        print(high_priority_machines[i], end=" ")

    print("\n")

    for i in range(1, l):
        c += 1
        print("Machine {} responding OK to the Election Message".format(high_priority_machines[i]))

    print("\nNo of machines responded OK to Election Message:", c)
    high_priority_machines.pop(0)

print("\nMachine {} elected as the New Coordinator\n".format(high_priority_machines[0]))

print("Machine {} sending message I am the New Coordinator to Machines ---->".format(high_priority_machines[0]),
      end=" ")

for i in range(1, no_of_machines):
    if (i == down_machine or i == high_priority_machines[0]):
        continue
    print(i, end=" ")