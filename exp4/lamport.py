'''
1. User se initial clock values li jaati hain  
   - Process 1 aur Process 2 ke clocks ka initial time input liya jaata hai.

2. Do important functions define kiye gaye hain  
   - `send(clock)`: Jab koi process message bhejta hai, to uska clock +1 hota hai.  
   - `receive(receiver_clock, sender_clock)`: Jab message receive hota hai, to receiver ka clock max(receiver, sender) + 1 hota hai (Lamport timestamp rule).

3. Ek `communication_queue` banayi gayi hai  
   - Ye ek queue hai jisme bheje gaye packets temporarily store hote hain jab tak koi receive nahi karta.

4. Menu-based simulation start hoti hai (while loop ke through)  
   - User ko options diye jaate hain:
     - Process 1 ya 2 packet bheje (send)
     - Process 1 ya 2 packet receive kare (receive)
     - Ya simulation exit kare

5. Send Operation:  
   - Jab bhi process 1 ya 2 koi packet send karta hai:
     - Clock +1 hota hai
     - Packet aur uska timestamp `communication_queue` me store hota hai

6. Receive Operation:  
   - Jab bhi koi process receive option choose karta hai:
     - Queue se pehla message nikala jaata hai
     - `receive()` function ke through logical clock update kiya jaata hai
     - Agar queue empty hai, to message milta hai: “No packets to receive.”

7. Clock Status Display:  
   - Har action ke baad, dono processes ke current clocks print hote hain taaki aapko pata chale kaunse time par kaunsa process hai.

8. Exit Option:  
   - User jab “Exit” choose karta hai, to simulation band ho jaata hai.
'''

# Initial clock inputs for both processes
clock_1 = int(input("Enter initial time for Process 1: "))  # Example: 2
clock_2 = int(input("Enter initial time for Process 2: "))  # Example: 5

print(f"\nProcess 1 initial time: {clock_1}")
print(f"Process 2 initial time: {clock_2}\n")

# Function to simulate sending a packet (increments clock)
def send(clock):
    clock += 1
    return clock

# Function to simulate receiving a packet
def receive(receiver_clock, sender_clock):
    return max(receiver_clock, sender_clock) + 1

communication_queue = []

# Simulation loop
while True:
    print("\n--- Menu ---")
    print("1. Process 1 sends packet")
    print("2. Process 2 sends packet")
    print("3. Process 1 receives packet")
    print("4. Process 2 receives packet")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        clock_1 = send(clock_1)
        communication_queue.append(('P1', clock_1))
        print(f"Process 1 sent a packet at time {clock_1}")

    elif choice == '2':
        clock_2 = send(clock_2)
        communication_queue.append(('P2', clock_2))
        print(f"Process 2 sent a packet at time {clock_2}")

    elif choice == '3':
        if communication_queue:
            sender, sender_time = communication_queue.pop(0)
            clock_1 = receive(clock_1, sender_time)
            print(f"Process 1 received a packet (from {sender}) at time {clock_1}")
        else:
            print("No packets to receive.")

    elif choice == '4':
        if communication_queue:
            sender, sender_time = communication_queue.pop(0)
            clock_2 = receive(clock_2, sender_time)
            print(f"Process 2 received a packet (from {sender}) at time {clock_2}")
        else:
            print("No packets to receive.")

    elif choice == '5':
        print("Exiting simulation.")
        break

    else:
        print("Invalid input. Try again.")

    print(f"Current Clocks -> Process 1: {clock_1}, Process 2: {clock_2}")
