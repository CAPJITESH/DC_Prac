'''
Step 1: Ek machine ko master elect karo (usually pehli machine hi hoti hai master)
Step 2: Master sabhi slave machines ko unka current time bhejne ke liye bolta hai
Step 3: Master sabhi machines ka time collect karta hai (including apna khud ka)
Step 4: Har machine ka skew calculate karo (Machine ka time - Master ka time)
Step 5: Sabhi skews ka average nikaalo (Master apne aap ko include nahi karta)
Step 6: Master new synchronized time calculate karta hai (based on average skew)
Step 7: Har machine ko batata hai ki kitna time add ya subtract karna hai
Step 8: Sabhi machines apna local time adjust kar leti hain (sync ho jaate hain)
'''

from datetime import datetime, timedelta

# Function to convert HH:MM to timedelta
def time_to_timedelta(time_str):
    hrs, mins = map(int, time_str.split(':'))
    return timedelta(hours=hrs, minutes=mins)

# Function to convert timedelta to readable time
def timedelta_to_time(td):
    total_seconds = int(td.total_seconds())
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"

# Input number of machines (including master)
n = int(input("Enter number of machines (including master): "))

# Input current times of all machines
machine_times = []
for i in range(n):
    t = input(f"Enter current time of Machine {i+1} (HH:MM): ")
    machine_times.append(time_to_timedelta(t))

# Assume first machine is master
master_time = machine_times[0]
print(f"\n[Master] Current Time: {timedelta_to_time(master_time)}")

# Calculate skews
skews = []
print("\nSkews (Difference from master):")
for i in range(1, n):
    diff = machine_times[i] - master_time
    skews.append(diff)
    print(f"Machine {i+1} skew: {int(diff.total_seconds() / 60)} minutes")

# Average skew (excluding master's own time)
total_skew = sum([s.total_seconds() for s in skews])
avg_skew = total_skew / (60 * (n - 1))  # in minutes
print(f"\n[Master] Average Skew: {avg_skew:.2f} minutes")

# Calculate new time to sync
new_master_time = master_time + timedelta(minutes=avg_skew)
print(f"[Master] New synchronized time: {timedelta_to_time(new_master_time)}")

# Send time adjustments
print("\nTime Adjustments:")
for i in range(1, n):
    adjustment = new_master_time - machine_times[i]
    new_time = machine_times[i] + adjustment
    print(f"Machine {i+1} adjusts by {int(adjustment.total_seconds() / 60)} mins → New Time: {timedelta_to_time(new_time)}")

# Master also adjusts its time
print(f"\n[Master] Adjusted Time: {timedelta_to_time(new_master_time)}")
